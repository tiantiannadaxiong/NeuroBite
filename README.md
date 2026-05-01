# NeuroBite

Neuroscience & AI 顶会论文速读笔记站。聚焦神经科学与人工智能交叉领域的前沿论文，提炼核心结论、方法主线、创新贡献与局限，让你一眼把握最新进展。

[访问站点](https://tiantiannadaxiong.github.io/NeuroBite/)

## 本地运行

```bash
bundle exec jekyll serve --livereload
```

## 内容结构

- `_posts/` — 所有论文速读笔记与采访记录，文件名格式 `YYYY-MM-DD-slug.md`
- `_posts/_PROMPT.md` — 论文速读 prompt 模板（11 节结构化分析）
- `_posts/_INTERVIEW_PROMPT.md` — 采访速读 prompt 模板（8 节结构化分析）
- `index.md` — 首页（hero + 最新 9 篇论文卡片 + 关于）
- `论文速读.md` — 全部论文存档页（permalink `/papers/`）
- `_layouts/` — Jekyll 布局模板
- `assets/css/neurobite.css` — 手写样式，无框架

## 技术栈

[Jekyll](https://jekyllrb.com/) 静态站点，部署于 [GitHub Pages](https://pages.github.com/)。推送 `main` 分支自动触发构建与部署。
