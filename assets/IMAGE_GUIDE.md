# 可视化素材对照说明

本目录按 README 叙事顺序组织。同名概念可能有多张图——层级不同，用途不同，**不应互相替代**。

## 电路/架构图层级

| 文件 | 来源 | 层级 | 展示内容 | README 用途 |
|------|------|------|----------|-------------|
| `02_architecture/fig1-7_framework.png` | 论文图 1-7 | 概念 | 生物感知→NAL→Hebbian/MMAM 信息流程 | **系统架构首选（思路层）** |
| `02_architecture/four_modules.PNG` | 结题 PPT | 概念 | SJ / NAL / EN / MMAM 四模块 | 模块功能对照 |
| `02_architecture/full_system.PNG` | 结题 PPT | 系统 | 三通道 SJ→NAL→EN + MMAM 总览 | 系统总览（PPT 版） |
| `04_innovation/full-orcad.png` | OrCAD 截图 | 实现 | 完整 PSpice 工程，含方向性标注 | **系统总览（工程版）** |
| `04_innovation/fig2-7_coexistence_circuit.jpg` | 论文图 2-7 | 模块 | 共存检测子电路 EC + AndEC | **共存检测专节** |
| `04_innovation/full_visio.jpg` | 论文图 2-8 | 模块 | MMAM 突触阵列 A + 检索 R | MMAM 原理 |
| `04_innovation/coexistence_mmam_concept.PNG` | 结题 PPT | 概念 | 共存检测 + 忆阻交叉阵列一页讲清 | 共存检测概念引导 |
| `04_innovation/coexistence_async_pulse_ch1.png` | 204组会 Slide 4 | 仿真 | 通道 1 异步脉冲串 | 与门失效说明（左） |
| `04_innovation/coexistence_async_pulse_ch2.png` | 204组会 Slide 4 | 仿真 | 通道 2 异步脉冲串 | 与门失效说明（右） |
| `04_innovation/coexistence_veng_gate.png` | 204组会 Slide 8–9 | 模块 | VPERM 门控 + VENG 输出电路 | 共存检测专节 |
| `04_innovation/coexistence_directional_weights.png` | 204组会 Slide 13 | 仿真 | M12/M21 等方向性阻值演化 | 方向性验证 |
| `04_innovation/research_outcomes_overview.PNG` | 结题 PPT | 摘要 | 三项研究成果文字总结（NAL/MSI/VR） | 成果概览，非电路图 |

### 关键辨析

**`full-orcad` vs `full_visio`**
- `full-orcad`：从 `Vs` 输入到 MMAM 输出的**完整可仿真工程**。
- `full_visio`：仅 MMAM 内部联想阵列与检索门控，不含三通道前端。

**`fig2-7` vs `coexistence_mmam_concept`**
- `fig2-7`：共存检测的**电路级原理图**。
- `coexistence_mmam_concept`：概念教学页，一页解释共存检测与 MMAM 关系。

**`full_system` vs `full-orcad`**
- 内容高度对应；前者 PPT 排版，后者 OrCAD 原始截图。

**`research_outcomes_overview`**
- 结题 PPT 研究成果摘要页。完整电路请用 `full-orcad.png` 或 `full_system.PNG`。

## 忆阻模型素材（128 组会）

README 忆阻专节采用**纯文字**说明，不嵌入图片。原始素材保留供追溯：

| 文件 | 来源 | 内容 |
|------|------|------|
| `07_memristor_model/slide7.png` | 128组会 Slide 7 | 原始窗函数边界锁死 |
| `07_memristor_model/slide8.png` | 128组会 Slide 8 | Biolek 方向性窗函数 |
| `07_memristor_model/slide9~10_text.txt` | 128组会 Slide 9–10 | 改进 SPICE 代码 |
| `docs/presentations/group-meetings/128组会ppt.pptx` | 组会归档 | 完整汇报 |

## 目录索引

```
assets/
├── 01_background/     Catalogue、生物学框架、文献对比表
├── 02_architecture/   ★ 图1-7 + 四大模块 + 系统总览
├── 03_units/          SJ / NAL / EN 单元验证
├── 04_innovation/     ★ 共存检测 + MMAM + OrCAD 全图
├── 05_msi/            多感官增强/抑制 + VR 检索
├── 06_applications/   痛觉感受器 + 语义饱和
└── 07_memristor_model/ 128组会原始素材（README 不引用图片）
```

## README 展示顺序

1. 项目概要 → 主要仿真结果 → 核心贡献
2. **忆阻模型改进**（文字）
3. **共存检测与方向性突触**（问题 → 信号分层 → EC/VENG → 方向性验证 → 图 2-7/2-8）
4. **系统架构**（图 1-7 → 四大模块 → full_system → full-orcad）
5. 仿真结果（含信号解读）→ 拓展应用 → 文献对比
