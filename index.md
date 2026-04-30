---
layout: default
title: NeuroBite
---

<div class="hero">
  <h1>NeuroBite</h1>
  <div class="tagline">神经科学 × 人工智能 · 顶刊论文速读</div>
  <div class="author-line">
    <svg viewBox="0 0 512 512" width="14" height="14"><path d="M488.6 104.1c16.7 18.1 24.4 39.5 23.3 65.5v202.4c-.4 26.4-9.2 48.1-26.5 65.1-17.2 17-39.1 25.9-65.5 26.7H92.02c-26.45-.8-48.21-9.8-65.28-27.2C9.682 419.4.767 397.5.968 371.7V169.2c-2.009-25.2 7.445-47.4 28.362-66.4l31.17-27.1 61.6-53.7c10.2-8.8 22.5-13.2 36.9-13.2 14.4 0 26.7 4.4 36.9 13.2l20.6 17.9h104l20.6-17.9c10.2-8.8 22.5-13.2 36.9-13.2 14.4 0 26.7 4.4 36.9 13.2l61.6 53.7 31.2 27.1zM390.3 159.1H121.7c-11.3 0-20.5 9.2-20.5 20.5v192.8c0 11.3 9.2 20.5 20.5 20.5h268.6c11.3 0 20.5-9.2 20.5-20.5V179.6c0-11.3-9.2-20.5-20.5-20.5zM221.3 313.6c-11.3 0-20.5-9.2-20.5-20.5v-48.2c0-11.3 9.2-20.5 20.5-20.5 11.3 0 20.5 9.2 20.5 20.5v48.2c0 11.3-9.2 20.5-20.5 20.5zm69.4 0c-11.3 0-20.5-9.2-20.5-20.5v-48.2c0-11.3 9.2-20.5 20.5-20.5 11.3 0 20.5 9.2 20.5 20.5v48.2c0 11.3-9.2 20.5-20.5 20.5z"/></svg>
    <span>天天拿大熊 @ B站</span>
  </div>
  <a href="#papers" class="hero-cta">浏览论文</a>
</div>

<div id="papers" class="section">
  <div class="section-title">最新论文</div>
  <div class="paper-list">
  {% assign papers = site.posts | sort: "date" | reverse %}
  {% for paper in papers limit: 9 %}
    <article class="paper-item">
      {% assign is_interview = paper.content_type == 'interview' %}
      {% if is_interview or paper.venue %}
      <div class="cat">
        {% if is_interview %}Interview{% endif %}{% if is_interview and paper.venue %} / {% endif %}{% if paper.venue %}{{ paper.venue }}{% endif %}
      </div>
      {% endif %}
      <h3><a href="{{ paper.url | relative_url }}">{{ paper.title }}</a></h3>
      <div class="meta">{{ paper.date | date: "%Y-%m-%d" }}</div>
      {% if paper.description %}
      <div class="excerpt">{{ paper.description }}</div>
      {% endif %}
    </article>
  {% endfor %}
  </div>
</div>

<div class="section">
  <div class="section-title">关于 NeuroBite</div>
  <div class="intro-text">
    <strong>NeuroBite</strong> 聚焦神经科学与人工智能交叉领域的前沿论文，每篇使用统一分析框架呈现核心结论、方法主线、创新贡献与局限，帮你快速判断是否值得精读。<br><br>
    在这里，我们不追求信息量，而追求<strong>认知效率</strong>。每一篇笔记都是一次对知识边界的勘探。<br><br>
    本站由 <span style="color: var(--bili); font-weight: 500;">天天拿大熊@B站</span> 策划与维护，内容同步更新于 Bilibili 与 GitHub。
  </div>
</div>
