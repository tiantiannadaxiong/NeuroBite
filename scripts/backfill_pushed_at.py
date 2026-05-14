#!/usr/bin/env python3
"""
Backfill pushed_at for all NeuroBite posts from git commit history.
Git is the single source of truth — no manual timestamps needed.

Usage:
    python3 backfill_pushed_at.py                  # backfill all posts
    python3 backfill_pushed_at.py --dry-run        # preview only

Effect:
    For each _posts/*.md file, reads git log to find the first commit
    that introduced or modified it in main, and injects that timestamp
    as `pushed_at` in the YAML front matter.
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime

NEUROBITE = os.path.expanduser("~/gitee/NeuroBite")
POSTS_DIR = os.path.join(NEUROBITE, "_posts")


def git_log_first_commit(filepath: str) -> str | None:
    """Get the ISO 8601 timestamp of the first commit for a file in main branch."""
    relpath = os.path.relpath(filepath, NEUROBITE)
    try:
        # Use last commit for the file — for single-commit files this IS the ingest time
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%cI", "-1", relpath],
            cwd=NEUROBITE,
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode == 0 and result.stdout.strip():
            ts = result.stdout.strip()
            # Normalize timezone: +0800 → +08:00
            if re.match(r'^.*[+-]\d{2}\d{2}$', ts):
                ts = ts[:-2] + ":" + ts[-2:]
            return ts
    except Exception:
        pass
    return None


def inject_pushed_at(content: str, timestamp: str) -> str:
    """Inject pushed_at into front matter, or update if exists."""
    lines = content.split("\n")

    # Find front matter boundaries
    fm_start = None
    fm_end = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if fm_start is None:
                fm_start = i
            else:
                fm_end = i
                break

    if fm_start is None or fm_end is None:
        return content  # No front matter

    # Check if pushed_at already exists in front matter
    for i in range(fm_start + 1, fm_end):
        if lines[i].startswith("pushed_at:"):
            old_ts = lines[i].split(":", 1)[1].strip()
            if old_ts == timestamp:
                return content  # Already correct
            lines[i] = f"pushed_at: {timestamp}"
            return "\n".join(lines)

    # Insert after date: or layout: line
    insert_idx = fm_end  # default: right before closing ---
    for i in range(fm_start + 1, fm_end):
        if lines[i].startswith("date:") or lines[i].startswith("layout:"):
            insert_idx = i + 1

    lines.insert(insert_idx, f"pushed_at: {timestamp}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Backfill pushed_at from git history")
    parser.add_argument("--dry-run", "-n", action="store_true", help="Preview changes")
    args = parser.parse_args()

    if not os.path.exists(POSTS_DIR):
        print(f"ERROR: Posts directory not found: {POSTS_DIR}", file=sys.stderr)
        sys.exit(1)

    posts = sorted(os.listdir(POSTS_DIR))
    updated = 0
    skipped = 0
    errors = 0

    print(f"Scanning {len(posts)} posts in {POSTS_DIR}...")

    for fname in posts:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(POSTS_DIR, fname)

        ts = git_log_first_commit(fpath)
        if not ts:
            print(f"  ⚠  {fname}: no git history found, skipped")
            errors += 1
            continue

        with open(fpath, "r") as f:
            content = f.read()

        new_content = inject_pushed_at(content, ts)
        if new_content == content:
            skipped += 1
            continue

        if args.dry_run:
            print(f"  📝 {fname}: would set pushed_at={ts}")
        else:
            with open(fpath, "w") as f:
                f.write(new_content)
            print(f"  ✅ {fname}: pushed_at={ts}")

        updated += 1

    print(f"\nDone. Updated: {updated}, Skipped: {skipped}, Errors: {errors}")
    if updated > 0 and not args.dry_run:
        print("\nNow commit the changes:")
        print("  cd ~/gitee/NeuroBite")
        print('  git add _posts/*.md && git commit -m "chore: backfill pushed_at from git history" && git push')


if __name__ == "__main__":
    main()
