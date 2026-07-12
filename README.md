# 面向多感官调制的非联想学习忆阻神经形态电路

> **Bio-Inspired Neuromorphic Circuit Design of Non-Associative Learning for Multisensory Enhancement and Depression**

蒋彦熙 · 哈尔滨工业大学 · 指导教师：王紫璐

`#忆阻器` `#神经形态电路` `#类脑计算` `#OrCAD` `#PSpice` `#非联想学习` `#多感官整合`

---

## 关于本项目

本项目实现了一套**可仿真的三通道忆阻神经形态电路**：在单块电路中串联非联想学习（NAL）→ 脉冲编码（EN）→ 共存检测（EC）→ 方向性多感官互联记忆（MMAM），覆盖习惯化/敏感化等前端调制、多感官增强与抑制（MSE/MSD）、跨模态检索（VR）及痛觉感受器、语义饱和等扩展场景。

**解决的痛点：** 现有忆阻神经形态方案常出现三类缺口——（1）忆阻模型触 Ron/Roff 后锁死，长时序仿真失败；（2）多感官整合只做增强、不做抑制；（3）异步脉冲下简单与门无法判定"是否共现"，且突触无方向性。本项目在器件模型、门控逻辑与系统验证三个层面给出可复现方案。

---

## 阅读指引

| 你关心什么 | 建议阅读 |
|--------|----------|
| 快速了解价值 | [项目概要](#项目概要) → [主要仿真结果](#主要仿真结果) → [核心贡献](#核心贡献) |
| 技术评审 | [忆阻模型改进](#忆阻模型改进) → [共存检测与方向性突触](#共存检测与方向性突触) → [仿真结果](#仿真结果) |
| 复现工程 | [环境配置](#环境配置) → [`circuits/`](circuits/) → [`simulation/`](simulation/) |
| 查阅全文 | [`docs/thesis/final/`](docs/thesis/final/) · [`docs/presentations/final/`](docs/presentations/final/) |

**术语速查：** NAL = 非联想学习；MMAM = 多感官互联记忆；MSE/MSD = 多感官增强/抑制；SJ/NAL/EN = 刺激判断 / 非联想学习 / 编码神经元单元；EC/AndEC = 共存检测 / 门控与逻辑。

---

## 项目概要

**在做什么**  
让忆阻器电路像生物感知一样：以非联想学习记住刺激强度变化，并以方向性区分通道先后，再靠共存检测判断是否该建立联想。

**解决了什么**  
修好忆阻器触界锁死，可反复调节；用共存检测替代简单与门，判定异步脉冲共现；以方向性突触阵列同时跑通增强、抑制与唤醒；非联想学习四过程与多感官整合同板验证。

---

## 主要仿真结果

<p align="center">
  <img src="assets/03_units/nal_four_processes.PNG" alt="NAL四过程" width="48%"/>
  <img src="assets/05_msi/memristor_array_innocuous.PNG" alt="MMAM阵列阻值" width="48%"/>
</p>
<p align="center"><em>左：NAL 四过程波形——习惯化衰减与敏感化/去习惯化跃变可见，说明前端通道可动态重编程。右：无害刺激下 MMAM 阵列阻值——三通道独立权值分化，共现增强写入成功。</em></p>

<p align="center">
  <img src="assets/05_msi/retrieval_vr.PNG" alt="VR跨模态检索" width="48%"/>
  <img src="assets/06_applications/nociceptor_waveforms.PNG" alt="痛觉感受器" width="48%"/>
</p>
<p align="center"><em>左：VR 检索脉冲——单通道线索可唤醒关联通道，验证跨模态联想。右：人工痛觉感受器——阈值、发放、适应等特性与生物痛觉模型一致。</em></p>

---

## 项目亮点

- **全链路可仿真**：OrCAD + PSpice 三通道系统，覆盖 SJ → NAL → EN → EC → MMAM 完整数据通路
- **两大核心改动**：忆阻模型边界锁死修复 + 共存检测子电路（详见下方专节）
- **功能完整性**：NAL 四过程 + MSE/MSD 双向整合 + 方向性跨模态检索，同板验证
- **可复现归档**：论文终稿、全部阶段 PPT、OrCAD 工程、仿真 CSV 与绘图脚本一并收录

---

## 核心贡献

| # | 贡献 | 说明 |
|---|------|------|
| 1 | **完整 NAL 四过程** | 习惯化 / 敏感化 / 去习惯化 / 自发恢复；同时考虑刺激**强度**与**价效** |
| 2 | **共存检测 + 方向性突触** | 时域 Hebbian 前提判定（EC/AndEC），区分 a→b 与 b→a，非对称驱动忆阻阵列 |
| 3 | **MSE + MSD** | 多感官共现增强、非共现抑制（多数文献仅 MSE） |
| 4 | **AIST 忆阻模型改进** | 正/负向 Biolek 窗函数分离 + 越界保护；见 [忆阻模型改进](#忆阻模型改进) |
| 5 | **高级仿生扩展** | 人工痛觉感受器（5 特性）、语义饱和（方向性双通道联想） |

**工作边界（供评审快速定位）：**

| 标签 | 内容 |
|------|------|
| **独立提出并实现** | 共存检测子电路（EC/AndEC）；方向性忆阻驱动（M12/M21/…）；Biolek 窗函数分向改进；语义饱和方向性联想方案 |
| **独立工程验证** | 三通道系统集成；NAL 四过程全测试；MSE/MSD/VR；人工痛觉感受器五特性 |
| **参考并实现扩展** | 多感官互联记忆（MMAM）总体框架与基础单元架构——见 [引用](#引用) |

> 探索性工作：新奇度通路已实现于 `circuits/memtest/somethingnew/saikai.opj`，见 [探索性分支](#探索性分支)。

---

## 忆阻模型改进

> 技术依据：[`docs/presentations/group-meetings/128组会ppt.pptx`](docs/presentations/group-meetings/) · [`docs/design-notes/电路设计推进.md`](docs/design-notes/电路设计推进.md)  
> SPICE 实现：[`circuits/memristor/zy_memristor/memristor_zhang.lib`](circuits/memristor/zy_memristor/memristor_zhang.lib)

电路采用 AIST 阈值忆阻模型，用内部状态变量 **x** 表征阻值在 Ron–Roff 间的相对位置。在 EN（ME 忆阻）与 NAL（MS 忆阻）联调中，原始实现存在**边界锁死**：统一窗函数 `f(x,p)=1-(2x-1)^(2p)` 在 x→0 或 x→1 时使 Gx 恒为零，阻值既不能继续增大也不能反向减小。

**影响：** MS/ME 触 Ron 或 Roff 后停止响应；Rinit 无法设为 Ron/Roff；长时序 NAL/EN 测试失败。

**改进方案：**

1. **分向窗函数**——正电压用 `f_inc`，负电压用 `f_dec`，分别约束上/下边界，契合 Biolek 原文中增阻/减阻表达式随电流方向变化的定义
2. **越界保护**——`stp()` 处理仿真步长导致的 x 滑出 (0,1) 区间

```spice
Gx 0 x value={ ... * f_inc(V(x),p) + ... * f_dec(V(x),p) }
.func f_inc(x,p)={1-x^(2*p)*stp(x)+stp(-x)}
.func f_dec(x,p)={1-(1-x)^(2*p)*stp(-x+1)+stp(x-1)}
```

| 对比项 | 原始模型 | 改进模型 |
|--------|----------|----------|
| 窗函数 | 单一 f(x,p)，x=0/1 双向锁死 | f_inc / f_dec 分向约束 |
| Rinit=Ron/Roff | 不可用 | 可用 |
| NAL/EN 边界行为 | 触界后失效 | 触界后可反向变化 |
| 数值鲁棒性 | x 越界时异常放大 | stp() 钳位保护 |

改进后 SJ / NAL / EN / MMAM 全部模块可稳定仿真，是 Chapter 4 系统级测试结果的前提条件。

---

## 共存检测与方向性突触

> 技术依据：[`docs/presentations/group-meetings/204组会ppt.pptx`](docs/presentations/group-meetings/) · [`docs/design-notes/关于突触链接建立的条件与方向性——MMAM单元前的判断机制.md`](docs/design-notes/)  
> 电路实现：`circuits/memtest/MMAM design/MMAM.opj`（图 2-7 共存检测 · 图 2-8 MMAM 单元）

本项目的**核心独立贡献之一**：在 MMAM 忆阻阵列写入之前，独立设计并实现了**共存检测子电路**，并配套**方向性突触门控**，解决异步脉冲条件下的赫布学习前提判定问题。

### 问题：简单与门无法判定"共现"

既有方案在 EN 与 MMAM 之间直接用与门判断"两路信号是否同时有效"。但经 EN **频率编码**后，各通道输出为等幅、异步、频率可不同的脉冲串——两路脉冲的峰顶往往**不在同一时刻**，与门输出恒为低，Hebbian 写入无法触发。

<p align="center">
  <img src="assets/04_innovation/coexistence_async_pulse_ch1.png" alt="通道1脉冲" width="45%"/>
  <img src="assets/04_innovation/coexistence_async_pulse_ch2.png" alt="通道2脉冲" width="45%"/>
</p>

*上图：两通道 EN 输出脉冲串。刺激时段重叠，但脉冲峰顶交错——简单与门无法检出共现，而共存检测可以。*

参考框架中同类设计假设脉冲已对齐，可直接求与；本设计面向**刺激时段重叠、脉冲异步**的真实编码输出，需另建判定逻辑（详见 204 组会 Slide 4–5）。

### 生物学依据

突触可塑性的有效时间窗约为 **20 ms** 量级（Bi & Poo, 1998），远大于单个动作电位宽度。因此"共现"应理解为：**两路活动在有效时间窗内存在重叠**，而非要求脉冲逐峰对齐。

### 信号分层：VPERM 与 VNE

共存检测将 EN 输出拆为两类信号（204 组会 Slide 7）：

| 信号 | 含义 | 作用 |
|------|------|------|
| **VNE** | 编码后的原生脉冲（神经元放电） | 供 COMP 比较器检测两路脉冲是否**时域重叠** |
| **VPERM** | 覆盖整段刺激期的使能窗 | 作为 PMOS 门控：仅当两路使能窗**同时有效**时，才允许输出共现脉冲 |

VNE 回答"脉冲有没有碰上"，VPERM 回答"刺激期是否重叠"——两者共同构成比与门更完整的共现判定。

### EC 模块：时域重叠检测

每对通道配置一个 **EC** 子模块（三通道系统含 EC1/EC2/EC3），核心链路：

```
VNEi + VNEj ──► COMP（比较器判定重叠）──► DFF（锁存时间窗）──► ECij 输出
```

- **COMP**：检测两路 VNE 在比较阈值以上是否存在时间重叠
- **DFF**：将重叠事件锁存为持续有效的时间窗（`VMEM` 状态）
- **EC 输出**：仅当"共现"成立时置高，作为后续 AndEC 的使能前提

论文图 2-7 即该子电路的完整原理图。

### VENG：共现成立后的统一驱动

当两路 **VPERM 均为高**（刺激期重叠）时，PMOS 关断，比较器将整流后的 **VNE** 与阈值比较，输出统一强度的 **VENG**（3 V 脉冲）；任一 VPERM 为低则 VENG 恒为 0。该级确保"共现"转化为可用于驱动忆阻的标准脉冲。

<p align="center">
  <img src="assets/04_innovation/coexistence_veng_gate.png" alt="VENG门控电路" width="75%"/>
  <br><em>VPERM 门控 + VNE 整流比较 → VENG（204 组会 Slide 8–9）</em>
</p>

### AndEC 门控与方向性突触

共现只说明"值得联想"，不说明"谁驱动谁"。**AndEC12 / AndEC13 / AndEC23** 在 EC 使能下，分别只允许对应方向的突触电压通过：

| 门控 | 驱动忆阻 | 含义 |
|------|----------|------|
| AndEC12 | M12 | 通道 1 → 通道 2 联想增强 |
| AndEC21 | M21 | 通道 2 → 通道 1 联想增强 |
| AndEC13 / AndEC31 | M13 / M31 | 通道 1 ↔ 通道 3 |
| AndEC23 / AndEC32 | M23 / M32 | 通道 2 ↔ 通道 3 |

因此语义饱和等场景只需激活**单通道**脉冲即可写入方向性权重，无需两路平均。OrCAD 工程中以 `Mab: 从a唤醒b` 标注各方向。

### 仿真验证：方向性权值独立演化

<p align="center">
  <img src="assets/04_innovation/coexistence_directional_weights.png" alt="方向性忆阻阻值" width="85%"/>
  <br><em>三对方向性忆阻（M21/M12、M23/M32、M31/M13）在 40 s 仿真中独立变化——共现时协同写入，单通道刺激时仅对应方向响应（204 组会 Slide 13）</em>
</p>

*解读：6.5 s 附近三路共现刺激触发协同阻值下降；36 s 附近仅蓝线（单通道）突降，绿/品红保持——证明方向性门控而非对称平均。*

### 概念与电路原理图

<p align="center">
  <img src="assets/04_innovation/coexistence_mmam_concept.PNG" alt="共存检测概念" width="90%"/>
  <br><em>共存检测 + 方向性忆阻交叉阵列（结题 PPT）</em>
</p>

<table>
<tr>
<td width="50%">

**图 2-7 · 共存检测子电路**

<img src="assets/04_innovation/fig2-7_coexistence_circuit.jpg" alt="图2-7" width="100%"/>

DFF 锁存时间窗 + COMP 判定 VNE 重叠；EC 输出作为 AndEC 使能，通过则允许赫布写入。

</td>
<td width="50%">

**图 2-8 · MMAM 单元**

<img src="assets/04_innovation/full_visio.jpg" alt="图2-8" width="100%"/>

突触互联阵列 **A** 存储联想权重，检索判断 **R** 产生 VR；PMOS 门控区分增强/抑制通路。

</td>
</tr>
</table>

---

## 系统架构

### 总体思路 · 图 1-7

<p align="center">
  <img src="assets/02_architecture/fig1-7_framework.png" alt="图1-7" width="95%"/>
  <br><em>生物感知 → 非联想学习 → 赫布联想 / MMAM 信息流程</em>
</p>

```
多通道刺激 ──► 非联想学习 (NAL) ──► 脉冲编码 (EN)
                      │                    │
                      └──────► 共存检测 (EC) ──► 方向性 MMAM 忆阻阵列 ──► VR / VM
```

### 四大电路模块

<p align="center">
  <img src="assets/02_architecture/four_modules.PNG" alt="四大模块" width="90%"/>
</p>

| 模块 | 功能 |
|------|------|
| **SJ** | 刺激强度阈值分类 + 价效（无害/有害）判断 |
| **NAL** | 习惯化 / 敏感化 / 去习惯化 / 自发恢复（忆阻 MH/MS） |
| **EN** | 电压→脉冲频率编码 + VM 使能 |
| **MMAM** | 共存检测门控 + 方向性忆阻阵列 → MSE / MSD / VR |

### 电路实现 · 三通道总体

<p align="center">
  <img src="assets/02_architecture/full_system.PNG" alt="PPT总览" width="90%"/>
  <br><em>结题 PPT：SJ → NAL → EN → EC/AndEC → MMAM 系统总览</em>
</p>

<p align="center">
  <img src="assets/04_innovation/full-orcad.png" alt="OrCAD工程" width="95%"/>
  <br><em>OrCAD 工程截图：含 <code>Mab: 从a唤醒b</code> 方向性标注的可仿真完整链路</em>
</p>

---

## 仿真结果

### 非联想学习（NAL）

<p align="center">
  <img src="assets/03_units/nal_four_processes.PNG" alt="NAL" width="85%"/>
</p>

*关键解读：重复无害刺激下响应逐步衰减（习惯化）；有害/高强度刺激触发敏感化跃升；去习惯化与自发恢复段可见阻值/输出反弹，四过程在同一单元内闭环验证。*

### 多感官整合（MSE / MSD）

<p align="center">
  <img src="assets/05_msi/memristor_array_innocuous.PNG" alt="阵列" width="45%"/>
  <img src="assets/05_msi/mixed_valence.PNG" alt="混合价效" width="45%"/>
</p>

*左图：共现刺激下对应交叉忆阻阻值下降（LTP 写入），非共现位置保持高阻——MSE 增强与 MSD 抑制同时可见。右图：混合价效下敏感化调制 EN 输出频率，放大 MMAM 写入强度差异。*

<p align="center">
  <img src="assets/05_msi/retrieval_vr.PNG" alt="VR" width="85%"/>
</p>

*单通道检索脉冲出现后，关联通道 VR 输出被唤醒；若联想未建立则 VR 保持静默——验证方向性存储可被选择性读取。*

---

## 拓展应用

> 以下基于 Chapter 5 电路架构，与核心系统并列验证信息处理能力，但不稀释 [核心贡献](#核心贡献) 中的两大改动。

| 人工痛觉感受器 | 语义饱和 |
|:---:|:---:|
| <img src="assets/06_applications/nociceptor_waveforms.PNG" width="100%"/> | <img src="assets/06_applications/semantic_satiation_overview.PNG" width="100%"/> |

*痛觉：阈值、发放率递增、适应等五特性与生物模型对照通过。语义饱和：方向性联想下重复激活导致 VR 衰减，分步现象见 `assets/06_applications/semantic_satiation_step1~4.PNG`。*

---

## 与现有工作对比

<p align="center">
  <img src="assets/01_background/comparison_table.PNG" alt="文献对比" width="90%"/>
  <br><em>现有研究与局限性——本文在完整 NAL、MSE+MSD、频率编码 EN、双向联想等维度上的差异化（详见配图标注）</em>
</p>

**本文相对现有忆阻神经形态工作的增量：**

- 完整非联想学习四过程 + 价效调制，而非单一突触可塑性演示
- 多感官**增强与抑制**双向整合，而非仅 MSE
- 共存检测 + 方向性突触，支持异步脉冲下的可控联想写入
- 编码单元面积 63.62 μm²，约为对照工作 [15]（129.61 μm²）的一半

---

## 仓库结构

```
.
├── README.md
├── assets/                     # GitHub 展示图片（见 IMAGE_GUIDE.md）
├── circuits/                   # 工程入口说明（README）；实体工程见 memristor/、memtest/
├── simulation/                 # CSV 数据 + draw.py 绘图脚本
├── docs/
│   ├── thesis/                 # final / drafts / submitted
│   ├── presentations/          # final / group-meetings / proposal-midterm / working-drafts
│   ├── design-notes/           # 设计笔记（共存检测、忆阻模型、新奇度等）
│   ├── reports/                # 开题 / 中期 / 行政材料
│   ├── references/             # 生物学 / 忆阻 / 神经形态参考文献
│   └── archive/                # 原文档归档、Visio 源、仿真截图
├── memristor/  memtest/  memdataprocess/   # 原始工程目录（路径保持不变）
```

---

## 环境配置

**环境：** OrCAD Capture 23.x + PSpice · Python 3.10+（可选，用于 CSV 后处理）

```
1. 克隆仓库，安装 Python 依赖（可选）
   pip install -r simulation/requirements.txt

2. 打开核心工程
   circuits/memtest/MMAM design/MMAM.opj

3. 运行基础仿真
   选择 NAL 或 MMAM 测试配置 → Run PSpice → 查看波形

4. 导出并可视化（可选）
   导出 CSV → python simulation/scripts/draw.py --csv <file>
```

| 工程 | 路径 | 内容 |
|------|------|------|
| 三通道完整系统 | `circuits/memtest/MMAM design/MMAM.opj` | 最终集成仿真 |
| 忆阻 SPICE 库 | `circuits/memristor/zy_memristor/memristor_zhang.lib` | 改进 AIST 模型 |
| 语义饱和 | `circuits/memtest/yuyibaohe/SemanticSatiation.opj` | 方向性联想应用 |

**常见问题：** 仿真不收敛时可检查 EN 输出频率是否过高导致步长过小；整合电路中 MOS 阈值需按 [`docs/design-notes/电路设计推进.md`](docs/design-notes/电路设计推进.md) 微调；确认已加载改进版 `memristor_zhang.lib`。

---

## 文档

| 文档 | 说明 |
|------|------|
| [`docs/thesis/final/`](docs/thesis/final/) | 论文终稿（PDF/DOCX） |
| [`docs/presentations/final/`](docs/presentations/final/) | 结题答辩 PPT |
| [`docs/presentations/group-meetings/`](docs/presentations/group-meetings/) | 组会材料：**128 组会**（忆阻模型）· **204 组会**（共存检测与方向性） |
| [`docs/presentations/`](docs/presentations/README.md) | 全部阶段 PPT 索引 |
| [`docs/design-notes/`](docs/design-notes/) | 设计笔记 |
| [`assets/IMAGE_GUIDE.md`](assets/IMAGE_GUIDE.md) | 可视化素材对照 |

---

## 引用

如使用本仓库内容，请注明：

> 蒋彦熙. 面向多感官调制的非联想学习忆阻神经形态电路设计的研究. 哈尔滨工业大学, 2026.

主要参考框架：

> Zhang Y., et al. *The Framework and Memristive Circuit Design for Multisensory Mutual Associative Memory Networks*. IEEE Transactions on Cybernetics, 2022.

---

## 探索性分支

[`circuits/memtest/somethingnew/saikai.opj`](circuits/memtest/somethingnew/) 实现了基于电容微分的新奇度检测通路（VNOV 并联叠加 + CMOPS 学习门控），设计说明见 [`docs/design-notes/非联想学习神经形态电路的生物合理性改进：引入新奇度机制.txt`](docs/design-notes/)。

该分支为**超纲扩展功能**的原理级原型，因开发周期未纳入主系统验证，保留作为后续研究方向。

---

## License

学术归档用途。论文版权归哈尔滨工业大学/作者所有。
