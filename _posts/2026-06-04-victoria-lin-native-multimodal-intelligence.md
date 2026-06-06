---
layout: post
title: "Victoria Lin × 原生多模态智能：表征困境与架构路线"
date: 2026-06-04
content_type: interview
venue: "Stanford CS25: Transformers United V6"
description: "多模态模型的scaling经验不能简单从语言模型迁移，理解与生成之间的表征鸿沟是当前最核心的理论障碍"
tags: [interview, multimodal, transformers]
---

## 0｜基本信息

- **受访者**：Victoria Lin，Technical Staff @ Thinking Machines Lab
- **背景**：前 Research Scientist @ Meta AI、Salesforce AI Research；PhD @ University of Washington
- **活动**：Stanford CS25: Transformers United V6 技术讲座
- **日期**：2026-06-04
- **形式**：60 分钟讲座 + 现场 Q&A
- **声明**：内容基于公开材料，仅代表个人观点，非雇主立场

> 这是一场技术密度极高的学术讲座，不是媒体采访。发表者系统梳理了 native multimodal 的技术谱系——从 discrete tokenization（Chameleon）到 AR+diffusion 融合（Transfusion）到模态分离参数（MoT）——并坦诚揭示了当前最棘手的开放问题：理解与生成的表征至今无法统一。

## TL;DR

1. **语言模型的 scaling 经验无法直接迁移到多模态**——next token prediction 在文本上催生了惊人的 emergent capabilities，但 next frame prediction 在视频上几乎不产生正向迁移，构成了多模态智能的核心悖论
2. **理解与生成的编码至今无法统一**——图像生成需要 VAE/diffusion 表征，图像理解需连续 encoder（如 SigLIP），两套编码互不兼容，是行业级开放问题
3. **MoT（Mixture of Transformers）是当前最 promising 的工程方案**——模态分离参数在非文本生成上显著优于同等规模 MoE，且不牺牲文本性能

## 1｜核心观点

**观点 1：仅靠语言建模不足以构建真正的通用智能**

- **支撑逻辑**：数字世界和物理世界充满多模态信息（图像、音频、视频、传感器数据），LM 只能处理文本这一种符号模态
- **声明类型**：`[个人判断]`
- **可信度**：高——领域共识

**观点 2：Native Multimodal 的核心范式是对所有模态统一做 tokenization → 全局 auto-regressive 建模**

- **支撑逻辑**：将图像 patchify → VQ-VAE 离散化或 continuous embedding → sequentialize，与文本 token 拼接后用同一套 Transformer 做 next-token prediction
- **声明类型**：`[推断]` — 从 Chameleon、Transfusion 等已发表工作中归纳
- **可信度**：高

**观点 3：离散化路线（Chameleon）图像信息损失显著，连续表征路线（Transfusion）是更好的权衡** ⚠️

- **支撑逻辑**：Chameleon 用 VQ-VAE 离散化后，图像理解与连续 encoder（SigLIP）存在明显 gap；Transfusion 在图像区域用 diffusion（continuous）显著提升生成质量、降低 token budget
- **声明类型**：`[第一手]` — 发表者参与相关工作
- **可信度**：高
- ⚠️ 但 Transfusion 用 VAE 表征适合生成却不利于理解，因此引入了理解-生成编码不统一的困境

**观点 4：模态间存在 capacity competition，MoT 通过模态分离参数缓解此问题**

- **支撑逻辑**：text 是高度压缩的符号系统，image 是稠密感知数据，统一参数难以同时最优处理两者。MoT 按 token 模态做 deterministic routing → 各自独立参数 → joint attention
- **声明类型**：`[推断]`
- **可信度**：高——163M–7B scaling ladder 系统验证

**观点 5：生成 → 理解的迁移几乎不存在，这是多模态领域最令人困惑的基本问题**

- **支撑逻辑**：Sergey Levine 推文："Puzzling that language models acquire amazing abilities through next token prediction, but video models don't get much stronger from next frame prediction"。假设解释：语言是人类认知的高度抽象压缩，sensory data 是被动观察，loss landscape 对人也不敏感
- **声明类型**：`[推断]`
- **可信度**：中高——引用了外部权威质疑，尚无严格理论解释

## 2｜话题分析

### 话题 1：语言模型的成就与边界

LLM 基于 next token prediction + scaling → emergent capabilities（知识获取、instruction following、CoT reasoning、planning）。但 LLM 无法直接处理文本之外任何模态。

### 话题 2：Native Multimodal 工程分类学

- **理解型模型**（Gemini、Qwen、Kimi）：多模态输入 → 文本输出
- **Omni 模型**（GPT-4o、Chameleon、Transfusion、Bagel）：多模态输入 → 多模态输出
- 核心理念：所有模态统一 tokenization → 统一序列建模

### 话题 3：三大架构路线

- **Chameleon（全离散化）**：VQ-VAE 将图像离散为 codebook tokens → 标准 cross-entropy LM 训练。优势：直接继承 LM 技术栈。缺陷：离散化信息损失大，token efficiency 差
- **Transfusion（AR + Diffusion 融合）**：同一 Transformer 内对文本做 AR modeling，对图像做 multi-step diffusion。图像质量显著更好，但 VAE 表征适合生成不适合理解——引入理解-生成编码 dilemma
- **MoT（模态分离参数）**：每个模态拥有独立 QKV projection + FFN 参数集，按 token 模态做 deterministic routing 后 joint attention。非文本生成显著优于同等参数 MoE，且不牺牲 text 性能

### 话题 4：理解与生成的编码困境

- 图像生成需 VAE/diffusion 表征（稠密、连续、适合去噪重建）
- 图像理解需 SigLIP 类连续 encoder（高语义、适合分类/推理）
- **目前没有任何一种编码能兼顾两者**——行业通常使用两套 encodings
- 这是远未解决的开放问题

### 话题 5：多模态作为 AI 新前沿

- **Bagel（2025 SOTA Omni 模型）**：采用 MoT 式架构，可先 "thinking text" 再生成图像，显著提升细节质量
- **具身 AI / 机器人**：MoT 被用于 action vector prediction（action 视为独立模态），基础 LM 知识通过 self-attention 传递
- **正向信号**：Vision-Language-Action (VLA) models 以 VLM 为 backbone 后显著提升

**提问者策略**：CS25 现场的 Q&A 质量极高，触及 MoT 信息流、JEPA 对比、text→image 渲染效率、人类 vs 模型学习方式的认知类比、以及"推理是否必须依赖文本"的终极问题。提问者主动提供反方论证（如 text→image 渲染的统一训练优势），体现了顶级学术沙龙的水平。

## 3｜关键数据与预测

**MoT 实证数据**
- 实验规模：163M → 7B 参数（多个中间规模），`[第一手]` → 可信度高
- MoT vs 4-expert MoE（非文本生成）：MoT 显著更优，`[第一手]` → 高
- MoT text 性能：与 dense baseline 相当，无退化，`[第一手]` → 高
- MoT 图像生成 loss：明显低于 dense，`[第一手]` → 高

**架构里程碑**
- Chameleon：首个 from-scratch interleaved text-image 训练，`[可核实]` → 高
- Transfusion：首个统一 AR + diffusion 于同一 Transformer，`[可核实]` → 高

**迁移关系**
- 理解 → 生成迁移：强力正相关，`[推断]` → 中
- 生成 → 理解迁移：几乎无正迁移，`[推断]` → 中 — 发表者坦诚尚未严格证明

**定性与预测**
- OCR text-as-image token efficiency：约 25 tokens/word，`[个人判断]` → 存疑，未实证
- 多模态 scaling law：远不如文本成熟，`[个人判断]` → 中（领域共识）
- 短期预测：越来越多特定能力定制化多模态模型；长期：需统一为 coherent system，`[个人判断]` → 中

## 4｜逻辑与依据评估

**整体逻辑强度：强**

- 论证结构清晰完整：动机 → 分类 → 技术路线 → 实证 → 开放问题
- 对每种架构的缺陷都做了坦诚评估，不回避关键问题
- 三个核心技术方案之间有清晰的对比逻辑（离散化 → VAE → 模态分离参数）
- Sergey Levine 的推文引用提供独立外部质疑锚点

**不足**
- MoT 的 deterministic routing vs soft/learned routing 的讨论缺失
- 音频/语音模态只在架构图中提及，缺乏具体实验结果
- 多模态 scaling law 为何与文本不同的理论分析停留在观察层面
- Q&A 环节对 "JEPA 对比" 的回答偏开放，缺乏具体技术对比

## 5｜弦外之音

| 观察 | 支撑证据 | 可能意味着 | 置信度 |
|------|---------|-----------|--------|
| 反复强调"个人观点，非雇主立场" | 开场声明 + 多处用 "in my opinion" | Thinking Machines Lab 可能有未公开内部方向，需明确切割 | 中 |
| 多个 Q&A 反复触及文本 vs 非文本关系 | Q3（视频→知识）、Q4（text→image 渲染）、Q9（推理依赖文本） | 文本在多模态中的"主导地位"是学术界最尖锐的分歧点 | 高 |
| 对"生成→理解迁移缺失"的回答语气明显更不自信 | 此处使用更多 hedging language（"I think" "maybe" "puzzling"） | 这是研究者自己也尚无答案的真开放问题 | 高 |
| Q4 中听者主动提出反方观点 | 提问者给出"统一模态训练更易稳定、OCR context 更短"等反驳 | 该议题在工业界可能已有内部实验数据 | 中 |
| 对 JEPA 的回答谨慎但开放 | "very interesting architecture" + "不同任务需要不同表征" | 发表者不认为 JEPA 是通用答案，但认可其在物理空间建模的潜力 | 中 |

## 6｜可操作信息

1. **MoT 架构是构建 Omni 模型的最优工程入口** — 模态分离参数路线已获 163M–7B 多规模验证，Bagel（2025 SOTA）采用类似设计。风险最低的起点
2. **理解-生成编码不统一是值得投入的高 impact 研究空白** — 这是一个无好解决方案的开放问题。SigLIP unified representation 的初探（2025）有 promise 但远未成熟
3. **不要指望训练图像/视频生成来提升理解/推理能力** — 生成→理解的正迁移被反复证伪，而理解→生成有强力正迁移。投入应优先放在理解端提升
4. **文本作为推理骨架在当前计算范式下仍有不可替代性** — Q9 辩论：视觉空间内做推理在计算和 UX 层面都不现实。神经科学视角可关注"抽象层约束"——人类认知是否有类似的模态隔离？

## 7｜一句话总结

**多模态模型远未被"搞定"，语言模型 scaling 的成功经验只解决了数字世界信息处理这一部分，物理世界智能需要全新的表征范式和训练框架——而理解与生成之间的表征鸿沟，是当前最核心的理论障碍。**
