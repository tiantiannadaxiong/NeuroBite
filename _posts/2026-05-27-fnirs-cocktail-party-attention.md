---
layout: post
title: "用可穿戴全头高密度fNIRS解码鸡尾酒会问题中的空间注意力"
date: 2026-05-27
venue: bioRxiv preprint (2026)
description: 用可穿戴全头高密度fNIRS系统，在单试次水平解码鸡尾酒会场景中的空间注意力方向，平均准确率76.5%，关键脑区为下顶叶
---

## 0｜基本信息（Metadata）
- **标题**: Decoding Spatial Attention in the Cocktail Party Problem Using Wearable Whole-head High-Density fNIRS
- **作者**: Sudan Duwadi, De'Ja Rogers, Alex D. Boyd, Laura B. Carlton, Yiwen Zhang, Anna Kawai Gaona, Aneesa Diya Pathiyaparambath, Ravin Chaudhury, Bernhard B Zimmermann, Walker J O'Brien (# deceased), Alexander von Lühmann, David A. Boas, Meryem A. Yücel, Kamal Sen
- **单位**: Boston University Neurophotonics Center (BME); TU Berlin; BIFOLD Berlin
- **发表**: bioRxiv preprint, 2026年5月11日; CC-BY 4.0; 未经过同行评审
- **DOI**: https://doi.org/10.64898/2026.05.06.722322
- **关联专利**: BU-2025-067, US Application No. 63/916,093

## 1｜核心结论（Core Takeaway）
使用可穿戴全头高密度fNIRS系统（ninjaNIRS22），可在单试次（single-trial）水平上稳健解码鸡尾酒会场景中受试者注意力的空间方向（左 vs 右）。21/26名受试者分类准确率高于随机水平，平均76.5%（范围52.3%–100%），解码延迟约2.5秒。**下顶叶（IPL），特别是左右角回（angular gyrus），是贡献最大的关键脑区**，仅使用IPL通道即可达到与全头通道相当的分类性能。

## 2｜研究问题与背景（Problem & Context）
- **鸡尾酒会问题（Cocktail Party Problem, CPP）**：在嘈杂多说话者环境中追踪目标说话者，是神经科学和人工智能语音识别的长期难题。听觉损失、ADHD、自闭症人群尤为困难。
- **空间注意力**被认为是解决CPP的核心机制。但人类大脑中支持CPP的空间注意力网络仍不清楚。
- 以往研究多使用纯视觉或纯听觉范式，缺乏生态效度。真实场景中视听多模态信息协同工作，且人们自然通过眼球运动定向注视目标（overt attention）。
- 既往fNIRS研究（Ning et al., 2024）在CPP场景中采集了初步数据，但未使用高密度系统，未监测眼动，也未识别关键皮层区域。

## 3｜方法主线（Approach）
1. **实验设计**：
   - 26名受试者（34人含对照组），坐在三台显示器前，左右各30°播放3秒视听电影片段（竞争说话者）
   - 2秒空间化白噪声+十字引导受试者注意左/右，允许眼球运动（overt attention）
   - 另设covert attention条件（仅听觉刺激，注视中心）和眼动控制条件
   - 共60个试次（左右各30），结束时回答音频/视频理解题

2. **fNIRS采集**：
   - 使用自研ninjaNIRS22系统：连续波、可穿戴全头高密度，56个光源+144个探测器，567通道/波长，760nm+850nm双波长，8.988Hz采样率

3. **数据预处理**：
   - Homer3 + Cedalion工具箱：原始强度质控 → 光密度转换 → TDDR运动校正 → 0.01–0.5Hz带通滤波 → 改良Beer-Lambert定律 → GLM估计单试次HRF

4. **分类方案**：
   - 二分类（Attend Left vs Attend Right），Random Forest分类器
   - d-prime排序选Top 20通道 → PCA降维 → 在1秒滑动窗口（步长0.5秒）提取PC时间序列的max amplitude + slope作为特征
   - 10次重复5折交叉验证，置换检验（1000次标签打乱）确定真实随机水平（下限40.7%，上限62.3%）

## 4｜创新贡献（Novel Contribution）
1. **首次使用可穿戴全头高密度fNIRS在单试次水平解码CPP空间注意力**，证明fNIRS在BCI和助听器场景中的可行性
2. **识别关键脑区**——下顶叶（IPL）/角回贡献最大，且仅用IPL通道即可达到全头性能，为设计紧凑型fNIRS设备奠定基础
3. **生态效度设计**：使用视听竞争说话者+自然眼动的overt attention范式，比纯听觉/纯视觉研究更贴近真实场景
4. **定量分离视觉和听觉成分**：overt vs covert对比揭示视觉成分对分类性能贡献占主导
5. **控制眼动贡献**：通过延长视觉定向与影片之间的延迟，证明IPL响应不能仅由眼动解释

## 5｜关键点（Key Points）
- **分类性能**：21/26人高于随机，均值76.5%（overt）；covert仅55.9%，显著低于overt（p<0.001）
- **解码延迟**：首次达到峰值95% CI下限的平均延迟为~2.5秒，在自然对话的行为相关时间尺度内
- **关键脑区ROI贡献排名**：
  1. 右角回IPL（平均贡献15%，100%受试者出现）
  2. 左角回IPL（平均贡献12%，100%受试者出现）
  3. 左视运动皮层/SPL
  4. 右前运动/辅助运动皮层
  5. 右上颞回（STG）
- **IPL仅用部分通道 vs 全头通道**：分类性能无显著差异（配对t检验，p=0.29）
- **变异性相关**：分类准确率与HbO单试次响应变异系数（CV）显著负相关
- **行为数据**：所有受试者行为正确率>70%，仅正确试次进入分析

## 6｜关键数学 / 统计方法（Quantitative Tools）
- **d-prime（d'）特征排序**：|μ₁-μ₂|/(加权合并标准差)，按0.7×峰值d' + 0.3×AUC复合指标选Top 20通道
- **PCA主成分分析**：PC时间序列的最大振幅和斜率作为分类特征
- **Permutation test**：1000次标签打乱估计真实随机水平（40.7%–62.3%）
- **PC-based feature importance**：平方载荷×解释方差比加权求和
- **Bonferroni校正**：HRF统计显著性检验的多重比较校正
- **GLM建模**：高斯基函数展开（间距1s，σ=1s）建模HRF，全局信号回归去噪
- **Coefficient of Variation (CV)**：σ/|μ|，量化试次间响应变异性

## 7｜结果与证据强度（Results & Evidence Strength）
- **强证据**：21/26（80.8%）受试者分类准确率显著高于随机水平，均值76.5%，说明fNIRS解码空间注意力是可行的
- **特征贡献清晰**：IPL/角回跨受试者一致性高（100%受试者出现），使用统计推断（置换检验、配对t检验）
- **控制实验充分**：同时进行了眼动控制、covert条件、行为正确率筛选
- **样本量一般**：26名受试者属于中等规模，性别比例不均衡（20男/6女）
- **注意**：overt decoding显著好于covert，表明当前方法对视觉成分依赖较大；covert条件解码能力有限（均值仅55.9%）

## 8｜局限与注意点（Limitations）
1. **仅二分类**：左vs右，未探索更多空间位置或更精细的分辨率
2. **Covert解码不佳**：纯听觉条件解码性能低，fNIRS cap可能未最优覆盖靠近耳朵的听觉皮层
3. **头部受限**：使用下巴托固定头部，不允许自然转头，生态效度仍有提升空间
4. **单模态fNIRS**：未融合EEG等互补模态，现有文献提示EEG-fNIRS融合可能进一步提升性能
5. **个体差异大**：准确率从52.3%到100%不等，部分受试者可能因试次间响应不一致性导致性能差
6. **性别偏差**：20男/6女，性别比例不均衡
7. **预印本状态**：未经同行评审
8. **Overt条件下眼动与注意力的叠加**：视觉定向和注意力机制的贡献难以完全分离（尽管补充实验部分回答了该问题）

## 9｜术语与表达（Jargon & Expressions）
| 术语 | 解释 |
|------|------|
| Cocktail Party Problem (CPP) | 鸡尾酒会问题：在多说话者嘈杂环境中追踪目标说话者 |
| fNIRS | 功能性近红外光谱，通过血氧浓度变化测量皮层活动 |
| High-density fNIRS | 高密度fNIRS，光源-探测器间距小，空间分辨率高 |
| Overt attention | 显性注意力：允许眼球运动定向注视目标 |
| Covert attention | 隐性注意力：注视中心不动，心理上注意某方向 |
| Inferior Parietal Lobule (IPL) | 下顶叶，包含角回和缘上回 |
| Angular Gyrus (AG) | 角回，IPL的一部分，本文最大贡献脑区 |
| Single-trial decoding | 单试次解码，对单个试验的血流动力学响应进行分类 |
| HRF (Hemodynamic Response Function) | 血流动力学响应函数 |
| TDDR | Temporal Derivative Distribution Repair，fNIRS运动校正方法 |
| d-prime | 信号检测论中的敏感度指标，衡量两类分离程度 |
| NinjaNIRS22 | 波士顿大学自研的可穿戴全头高密度fNIRS系统 |

## 10｜可迁移价值（Transferable Value）
1. **BCI/助听器**：解码空间注意力可用于"steering"助听器等辅助设备，对准用户关注的声源
2. **紧凑型硬件设计**：IPL是关键区域→可设计仅覆盖IPL的简洁fNIRS设备
3. **AR/VR注意力引导**：注意力引导的视音频渲染资源分配
4. **BOSSA算法对接**：本文团队此前提出的BOSSA（脑启发声源分离算法）需要用户关注空间位置作为输入，fNIRS解码可提供此信息
5. **方法论**：d-prime+PC贡献的通道选择方法可推广到其他fNIRS解码研究

## 10｜一句话总结（One-line Summary）
用可穿戴全头高密度fNIRS可在单试次水平以76.5%准确率解码鸡尾酒会中的空间注意力方向，下顶叶（IPL）是最关键的脑区。
