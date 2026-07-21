---
layout: post
title: "Evo 2 — 跨生命域的全基因组基础模型"
date: 2026-03-04
venue: "Nature"
description: "在全生命域 9.3T DNA token 上训练的基因组基础模型，百万碱基上下文窗口，零样本预测致病突变并可引导设计染色质可及性"
---

## 0｜基本信息（Metadata）

- **标题**：*Genome modelling and design across all domains of life with Evo 2* / 《Evo 2：跨生命域的基因组建模与设计》
- **作者**：Garyk Brixi, Matthew G. Durrant, Jerome Ku, Mohsen Naghipourfar, Michael Poli, Gwanggyu Sun（共同一作）et al. 通讯作者 Patrick D. Hsu（Arc Institute / UC Berkeley）& Brian L. Hie（Arc Institute / Stanford）
- **期刊**：Nature（主刊），Vol 652, 30 April 2026
- **发表时间**：2026 年 3 月 4 日 online

---

## 1｜核心结论（Core Takeaway）

Evo 2 是迄今为止**最大的开放基因组基础模型**（40B 参数），在涵盖细菌、古菌、真核生物和噬菌体的 9.3 万亿 DNA token 上训练，拥有 **100 万碱基上下文窗口**、单核苷酸分辨率。它无需微调即可零样本预测从非编码致病突变到 BRCA1 临床变异的功能影响，能生成线粒体（16kb）、原核（580kb）和真核（330kb）尺度基因组序列，并通过推理时搜索+Enformer/Borzoi 引导设计染色质可及性模式——**经 ATAC-seq 实验验证**。

---

## 2｜研究问题与背景（Problem & Context）

- **核心问题**：基因组编码了生命的所有信息，但我们对它的理解远不足以预测各种基因组改变的影响，或智能设计新的生物系统
- **已有方案**：Evo 1 展示了原核基因组的序列建模+设计潜力，但**无法处理真核基因组**（更复杂、更长程的相互作用，如内含子-外显子结构、增强子-启动子远程调控）
- **为什么难**：真核基因组需要百万碱基量级的上下文才能捕捉远程调控元件与染色质结构；同时，现有模型要么限于特定物种/模态，要么需要人工标注

---

## 3｜方法主线（Approach）

**数据 → 架构 → 训练 → 评估 → 应用**

1. **OpenGenome2 数据集**：8.8+ 万亿核苷酸，覆盖细菌（Pseudomonadota/Bacillota 等）、古菌（Thermoproteota 等）、真核（脊索/节肢/链形植物/真菌）、细胞器基因组，以及 phage/ncRNA
2. **StripedHyena 2 架构**：不同于纯 Transformer，使用三种卷积 Hyena 算子混合（short explicit + medium regularized + long implicit）+ attention 的**多混合架构**，在 40B 规模 1M 上下文下比 Transformer 快 3×
3. **两阶段训练**：先 8K 上下文预训练（聚焦基因区），再多阶段中训练扩展到 1M 上下文（捕捉长程互作）
4. **评估线**：零样本变异效应预测（ClinVar/DMS/BRCA1/BRCA2/SpliceVarDB）、嵌入分类器（外显子/基因必需性）、SAE 机制可解释性、无条件生成 + 推理时引导设计
5. **生物安全**：**排除感染真核宿主的病毒序列**以降低滥用风险，并通过 red teaming 验证模型无法有效生成人类病毒蛋白

---

## 4｜创新贡献（Novel Contribution）

**系统级创新，幅度大**：

1. **首个覆盖全部生命域的基因组基础模型**：不是真核专用，也不是原核专用，而是统一
2. **百万碱基上下文 + 单核苷酸分辨率**的基因组语言模型——可以同时捕捉启动子（~100bp）和 TAD（~1Mb）级别的模式
3. **机制可解释性（SAE）的规模化应用**：首次在基因组语言模型上系统展示 SAE 特征对应已知生物概念（噬菌体区域、外显子边界、转录因子结合基序、蛋白二级结构）
4. **推理时引导设计染色质可及性**：Evo 2 生成 + Enformer/Borzoi 评分 + beam search → **实验验证** ATAC-seq，达到 AUROC 0.92-0.95

---

## 5｜关键点（Key Points）

1. **零样本变异预测显著超越同类模型**：ClinVar 编码区 non-SNV 所有方法第一；非编码区 SNV 无监督模型第一；BRCA1 非编码区所有模型第一；BRCA1 编码区零样本 AUROC=0.95（supervised 版本）
2. **SAE 揭示 70% 的人类启动子富集基序**（HOMER 只回召 35%），特征跨物种泛化（人→猛犸象基因座）
3. **生成能力跨尺度验证**：线粒体（16kb）正确产生 13 CDS + 22 tRNA + 2 rRNA 并保持同线性；M. genitalium（580kb）70% 基因有 Pfam hit（Evo 1 仅 18%）；酵母染色体（330kb）含内含子基因
4. **染色质设计实验验证**：合成 DNA 定入小鼠基因组，ATAC-seq 实测 AUROC=0.92-0.95（Morse code "EVO2""LO""ARC"）；跨细胞系（HEK293T/K562）36 个设计 92% AUROC>0.8
5. **生物安全设计有效**：排除真核病毒感染相关序列后，模型在人类病毒蛋白生成上表现为随机水平，且零样本毒力预测无相关性

---

## 6｜关键数学 / 统计方法（Quantitative Tools）

1. **StripedHyena 2**：基于 Hyena（输入相关长卷积）的多混合架构，不使用纯自注意力。在长序列下比 Transformer 吞吐量提升 3×，比 StripedHyena 1 有更好的 loss scaling
2. **Batch-TopK Sparse Autoencoder（SAE）**：在 Evo 2 layer 26 的表示上训练，提取稀疏高维特征，每个潜在维度对应可解释的生物模式。训练数据来自多个完整真核/原核基因组，共 10 亿 token
3. **推理时 beam search + Enformer/Borzoi 评分**：不修改模型权重，每次生成 128bp 后评分择优——发现 log-linear 关系：beam search 宽度增加→设计质量提高，**在生物设计中展示了 inference-time scaling law**

---

## 7｜结果与证据强度（Results & Evidence Strength）

**高强度**。理由：

| 维度 | 评价 |
|------|------|
| 规模 | ⭐⭐⭐⭐⭐ 9.3T token 训练，40B 参数，1M 上下文 |
| 评估广度 | ⭐⭐⭐⭐⭐ 零样本预测（ClinVar/DMS 等 20+ 基准）、外显子分类（8 个 held-out 物种 AUROC 0.91-0.99）、基因必需性、生成质量（多个计算指标） |
| 实验验证 | ⭐⭐⭐⭐ 染色质设计有合成+ATAC-seq 验证（36 个设计）；但生成基因组缺乏功能性验证（合成生物学实验未完成） |
| 对照 | ⭐⭐⭐⭐⭐ 在每项任务上与其他 20+ 模型全面对比（ESM/ProGen/NT/GPN-MSA/CADD/AlphaMissense/SpliceAI 等） |
| 因果性 | ⭐⭐⭐ 相关工作观察性为主，SAE 特征与生物标注的关联基于富集分析而非因果验证 |
| 安全性 | ⭐⭐⭐⭐⭐ 有系统性风险评估（red teaming、祖先偏倚、病毒排除验证） |

> 综合：Evo 2 的零样本预测能力（尤其在 non-SNV 和非编码变异上）和计算生成能力令人印象深刻，但**全基因组设计的真实性评估仍限于计算指标**。

---

## 8｜局限与注意点（Limitations）

1. **生成基因组缺乏功能性验证**：虽然 M. genitalium 和酵母染色体在计算指标上看起来合理，但生成的序列缺少一些必需基因，距功能完整的合成基因组还有距离
2. **调控区零样本预测仍有瓶颈**：远端调控变异的预测不及 ChromBPNet 等序列-功能模型（DART-eval）
3. **SAE 特征局限于当前标注知识**：无标注的 genomic dark matter 中可能存在更有趣的特征，但方法目前依赖于已知标注的对比搜索
4. **推理时引导的计算成本高**：beam search 80+ tokens/bp 才达到最优，大规模设计可能需要 100 倍以上的推理计算

---

## 9｜术语与表达（Jargon & Expressions）

> **foundation model** → 基础模型（在大规模数据上预训练后可用于多种下游任务）
> **zero-shot prediction** → 零样本预测（不经过任务微调直接推断）
> **sparse autoencoder (SAE)** → 稀疏自编码器（从模型表示中分解出稀疏、可解释的特征）
> **inference-time guidance** → 推理时引导（生成时通过评分函数筛选，不修改模型权重）
> **stripedHyena** → 多混合卷积架构（使用三种不同尺度的输入相关卷积算子）

---

## 10｜可迁移价值（Transferable Value）

1. **多混合架构选型思路**：StripedHyena 2 证明在长序列生物序列任务上，精心设计的卷积混合可以比纯注意力更高效——对计算受限的领域有借鉴意义
2. **SAE 用于基础模型透明化**：通用方法→任何大型生物学模型都可以训练 SAE 做特征发现，潜力巨大
3. **推理时搜索 + 领域评分模型的通用范式**：Evo 2 + Enformer 的设计管线可推广到任何有评分模型的生物设计任务（蛋白设计、代谢通路设计等），无需重新训练生成模型
4. **开源全部组件（数据+代码+权重）**作为开放科学的范例

---

## 11｜一句话总结（One-line Summary）

**Evo 2 是一个在全生命域 9.3T 碱基上训练的开放基因组基础模型（40B 参数、百万上下文窗口），能零样本预测致病突变、生成跨尺度基因组序列，并通过推理时搜索指导实验验证的染色质设计。**
