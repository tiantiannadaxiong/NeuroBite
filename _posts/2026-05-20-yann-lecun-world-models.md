---
layout: post
title: "Yann LeCun × LLM 之后：世界模型、JEPA 与 AMI Labs"
date: 2026-05-20
content_type: interview
venue: "Unsupervised Learning (Redpoint AI)"
description: "LeCun离开Meta创立AMI Labs，押注JEPA世界模型。LLM不是通往人类智能的路——它们天生不安全。"
tags: [interview, AI, world-models]
---

## 0｜基本信息（Metadata）

- **受访者**：Yann LeCun — Meta 前首席 AI 科学家、图灵奖得主，现 AMI Labs（Advanced Machine Intelligence）创始人兼 CEO
- **采访者 / 媒体**：Jacob Effron / Unsupervised Learning（Redpoint AI 旗下播客）
- **采访时间**：2026年5月15日发布
- **采访背景**：LeCun 近期离开 Meta 创立 AMI Labs，专注 JEPA 架构与世界模型。本期访谈覆盖他离开 Meta 的原因、JEPA 技术路线、AI 安全立场、与 Hinton/Bengio 的分歧、以及他对 LLM 和开源 AI 格局的长期判断。

---

## TL;DR｜核心结论速览

1. **LeCun 认为 LLM 本质上是死胡同**——对文本操作极好，但无法预测自身行为的后果，不具备规划能力，不是通往人类级智能的路径
2. **JEPA 世界模型的技术赌注是：在表征空间（而非像素空间）中做预测**，以此绕过生成模型的固有缺陷
3. **LLM 天生不安全**——无法杜绝幻觉，无法保证 agentic 行为的安全性，这一观点比 Hinton/Bengio 的"AI 灭绝论"更具体但也更激进

---

## 1｜核心观点（Core Views）

**观点一：LLM 不是通往人类级智能的路径**

LeCun 反复强调这一立场——不是否定 LLM 的实用价值，而是断言其架构上限。核心支撑：LLM 通过逐 token 自回归生成运作，**本质上无法预测自身行为的后果**，也没有规划能力（planning by search）。`[个人判断]`

- **支撑逻辑**："If you have a sequence of discrete symbols, making predictions is easy... the real world is high-dimensional, continuous, noisy, messy." LLM 恰好活在"离散符号的低维流形"里——语言本身是简化的。
- **可信度判断**：逻辑自洽，有充分的实验结果支撑（JEPA vs 生成模型的对比）。但这是 LeCun 十年如一日的立场——偏差明确。

**观点二：VLA（Vision Language Action）已被证明失败**

声明简短但直接——"VLA is clearly now being seen as not going anywhere." 不可靠、需要过多训练数据。`[个人判断]`

- **支撑逻辑**：imitation learning 的思路无法泛化至新任务，缩放数据也解决不了根本问题。
- **可信度判断**：行业内对此观点分歧很大——Google 和 Physical Intelligence 仍在重投 VLA 路线，可见 LeCun 的结论为时过早。

**观点三：LLM 在本质上不安全**

**"LLMs are intrinsically unsafe. I don't think they can be made reliable and safe."** `[个人判断]`
- **支撑逻辑**：无法阻止幻觉 + 无法预测行动后果 + 无法在 prompt 外强行施加约束。举例：coding agent 随手清空硬盘；"洗车离我家 100 米，该走路去吗"所有 LLM 回答"是"（除了德国版本）。
- **⚠️ 与公开信息存在出入**：Anthropic/OpenAI 投入大量资源做 RLHF、constitutional AI、red-teaming，声称可大幅降低风险。LeCun 认为这些是"打补丁"，不能解决根本问题。

**观点四：开源 AI 将重复 Linux 的历史**

将今天的 OpenAI/Anthropic 比作 1996 年的 Sun Microsystems/HP——"the entire internet runs on Linux." `[推断]`
- **支撑逻辑**：①公开文本数据已耗尽，封闭模型的优势来自许可数据而非架构革命 ②大多数国家需要主权 AI，不接受美中的封闭平台 ③AI 正快速成为基础设施平台，平台天然趋向开放
- **可信度判断**：强的历史类比。但 1996 年 Linux ≠ 2026 年 AI——训练基础设施的资本壁垒高出几个数量级。

**观点五：AMI Labs 的目标是"AI for the real world"——短期工业应用，长期通用具身智能**

- **短期**：为工业系统（喷气发动机、化工厂、制造线）构建世界模型——理解复杂系统动态，优化控制。
- **长期**：家用机器人、L5 自动驾驶（"several years down the line"）。
- **内部代号**：项目在 Meta 内部就叫 AMI（Advanced Machine Intelligence），然后变成公司名。

---

## 2｜话题分析（Topic Breakdown）

### 话题一：LeCun 离开 Meta 的真实原因

- **核心信息**：不是单一事件，而是多重因素的累积：①Meta 全公司重心转向 LLM，探索性研究被降级 ②Meta 解散了机器人 AI 团队（Gita Matalatic 去了 Amazon） ③FAIR 逐渐被要求全力支持 GenAI 的 LLM 工作 ④大部分 JEPA 应用场景在工业领域，Meta 不感兴趣
- **关键细节**：Mark Zuckerberg 和 CTO Andrew "Buzz" Bosworth 实际上支持 JEPA 项目——"a lot of support in the leadership"——但中层以下"didn't see the point"
- **值得注意**：LeCun 明确否认了媒体叙事中"Alexandre 来后 LeCun 被边缘化"的说法。**他对 LLaMA 零技术贡献**，唯一的大贡献是推动 LLaMA 2 开源（"与法务部数月的高层拉锯"）。内部代号 AMI 在 Meta 内部启动，离开几个月后 AMI Labs 成立。

### 话题二：JEPA 的技术路线——在表征空间中预测

- 核心创新不在于架构本身，而是**放弃了像素级预测**（VQ-VAE、masked autoencoder 等被描述为"非常令人失望"）
- 最大的技术挑战是 **representation collapse**——两个编码器简单学出常数解。LeCun 2026 年仍在探索哪些 collapse 预防方法真正工作：contrastive learning（1993 年他提出的，但维度扩展性差）、mutual information maximization（Hinton/Becker 90s）、distillation methods（DINO——"we don't know why it works"）
- **提问者策略**：Jacob 表现出明显的技术理解力，追问点集中在架构选择和工程可行性。未追问的关键问题：JEPA 在视频/机器人任务上的具体 benchmark 结果。

### 话题三：与 Hinton/Bengio 的分歧起点——GPT-4

- **戏剧性转折**：LeCun 说"我没改变想法，他们改变了。" 2023 年 GPT-4 发布是分水岭。
- **Hinton 的"epiphany"**：用"脑皮层 16B 神经元 × 10 个生物神经元 ≈ 1 个反向传播神经元"的粗糙计算得出 GPT-4 快赶上人类。
- **LeCun 的回应**：不认同这个计算。"我觉得 Hinton 基本上是在说'我可以退休了'" ——讽刺意味明显。
- **Bengio**：也担心 AI 利益分配不均和滥用，而非 AI 取代人类。LeCun 认为这是合理的担忧，但远不如 Anthropic 渲染的末日论。

### 话题四：开源 vs 封闭 AI 格局

- 公开文本数据已耗尽——封闭公司的唯一优势来自许可数据或合成数据
- 提出了一种**去中心化共识训练**框架：多个参与方定期交换参数向量，汇聚成全球共识模型。这使得小体量参与者也能得到接近全数据训练的模型质量
- 每个参与者可用共识模型 fine-tune 自己的文化/语言/政治倾向版本
- 关键比较：Sun vs Linux → 封闭 vs 开源 AI

### 话题五：AI 安全的真实分歧

- LeCun 认为 LLM 天生的不可靠性比 Superintelligence 风险更紧迫
- **明确指责 Anthropic** "lobbying governments into scaring them into regulating AI"——认为商业利益驱动了末日论叙事
- 但世界模型架构本身也引发安全问题——只是 LeCun 认为可控性强得多，因为可以显式建模行动后果

---

## 3｜关键数据与预测（Key Data & Predictions）

| 内容 | 数值 / 时间节点 | 声明类型 | 来源可信度 |
|------|----------------|---------|-----------|
| LLM 数据已耗尽（公开文本） | 2025-2026 | [第一手] | 高 — 行业共识 |
| 人类学会开车需 | ~20 小时 | [可核实] | 高 |
| JEPA 研究 5-6 年加速 | 2020-2026 | [第一手] | 高 |
| 家用机器人/L5 自动驾驶实用化 | "several years down the line" | [个人判断] | 低 — 模糊时间线 |
| "5 年完全统治世界"（调侃 Linux 引用） | 5 年 | [访谈调侃] | 不适用 |
| AMI Labs 已打动大量 VC | 2026 年初完成融资（推断） | [第一手] | 中 — 未披露具体金额 |

---

## 4｜逻辑与依据评估（Logic & Evidence）

- **核心一致性**：强。LeCun 对 LLM 局限性的判断与他 2016 年至今发表的演讲/论文完全一致。没有明显的立场变化或自我矛盾。
- **论证强度分布不均**：对 LLM 架构上限的理论论证（无规划能力、不能预测行动后果）较强且有机制性解释；对 JEPA 商业成功的时间线论证极弱（"5 年统治世界"是玩笑，但严肃的时间表几乎为零）。
- **缺失证据**：JEPA 在真实世界任务上的系统 benchmark 几乎没有。LeCun 用"大量已有结果"搪塞——对于一个刚拿到融资的创业公司而言，这个缺失很关键。
- **⚠️ 逻辑漏洞**：LeCun 批评 LLM 不能预测行动后果，但 JEPA 目前只在静态图像/视频表征上验证，离"行动条件预测"还有一条很长的路。他把"应该能做到"等同于"做到了"。
- **整体逻辑强度：中**。理论论证有力，但证据基础薄弱。

---

## 5｜弦外之音（Reading Between the Lines）

| 观察 | 支撑证据 | 可能意味着 | 置信度 |
|------|---------|-----------|--------|
| 反复强调"我对 LLaMA 零贡献" | 三次明确声明 + 强调唯一贡献是推动开源 LLaMA 2 | **正在管理市场叙事**，防止 LLaMA 的成功被归功（或归咎）于他，同时也与 Meta 的 AI 成就切割 | 高 |
| 总部设在巴黎、纽约办公室，特意避开了硅谷 | 明确说出"deliberately not Silicon Valley" | 人才反周期策略 + 意识形态拒绝（硅谷的"herd behavior"）——但也意味着承担更小的人才池和高管网络 | 中 |
| 对 VLA 的否定语气异常坚决 | "clearly now being seen as not going anywhere" 用现在时态 | 他可能在与 Physical Intelligence 或 Google DeepMind 的 VLA 团队直接竞争，否定 VLA 就是在否定对手跑道 | 中 |
| 提到"FAIR 的人也在走"时语气明显情绪化 | "a lot of good people have left already" | 离开 Meta 不只是战略分歧——他对 FAIR 被"降级为 LLM 支援组"的管理层决定感到失望和受伤 | 高 |
| 指控 Anthropic 有商业动机渲染 AI 风险 | "brainwash some people and government into thinking their systems are dangerous" | 这是**对 Anthropic 最直接的人身攻击**——超出技术分歧，进入道德指控 | 高 |

---

## 6｜可操作信息（Actionable Takeaways）

1. **JEPA/World Model 赛道正在从研究走向创业**：LeCun 不是唯一——Jerry Tworek、David Ha 等也在类似方向创业。这意味着未来 1-2 年将有多家"后 LLM"架构创业公司并行融资。作为投资人/研究员，应系统梳理这个领域的公司图谱。
2. **LLM 的"数据天花板"已被 LeCun 公开确认**：公开文本数据耗尽——这解释了为什么 OpenAI/Anthropic 越来越强调 reasoning（用更少数据产生更多价值）以及 licensing deal（Reddit、新闻集团）。这是 LLM scaling 的第一性原理约束。
3. **LeCun 的争议性观点可能影响欧洲 AI 政策**：作为法国人 + 巴黎总部 + 对"AI 安全监管游说"的公开批评 → 可能会被欧洲立法者用作放松 AI Act 执行的学术论据。
4. **Anthropic 的"AI safety"叙事面临反驳压力**：LeCun 的公开指控（商业利益驱动末日论）在学术界有相当共鸣。如果更多图灵奖级人物加入质疑，Anthropic 的政策游说策略可能被迫调整。
5. **Meta AI 的人才流失信号需要关注**：LeCun + Gita Matalatic（Amazon）+ 多位未提名的研究员离开→FAIR 在 LLM 军备竞赛中可能失去探索性研究的文化，间接利好 Anthropic 和 Google DeepMind。

---

## 7｜一句话总结（One-line Summary）

> LeCun 用 AMI Labs 对赌一个信念：LLM 的离散符号天堂不能延伸到三维物理世界的连续混乱——但 JEPA 能否真正跨过这条鸿沟，他还没给我们看到数据。
