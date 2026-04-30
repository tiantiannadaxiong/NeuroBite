# Squash git history and preserve repo identity

$remoteUrl = git remote get-url origin
# Extract username and email from remote config
$userName  = git config user.name
$userEmail = git config user.email

# If not set locally, fall back to global config
if (-not $userName)  { $userName  = git config --global user.name }
if (-not $userEmail) { $userEmail = git config --global user.email }

# Extract GitHub username from remote URL
# Supports both HTTPS and SSH formats
if ($remoteUrl -match "github\.com[:/](.+?)/") {
    $githubUser = $Matches[1]
} else {
    Write-Error "Could not extract GitHub username from remote URL: $remoteUrl"
    exit 1
}

# Use GitHub username if no local/global name is set
if (-not $userName) { $userName = $githubUser }

Write-Host "Remote URL : $remoteUrl"
Write-Host "Git user   : $userName"
Write-Host "Git email  : $userEmail"
Write-Host ""

# Apply user config locally to this repo
git config user.name  $userName
git config user.email $userEmail

# Squash all history into a single orphan commit
git checkout --orphan fresh-start
git add -A
git commit -m "Initial commit"

# Replace main branch (adjust if your branch is 'master')
git branch -D main
git branch -m main

Write-Host "Force pushing to origin..."
git push origin main --force

Write-Host "Done. History cleared."