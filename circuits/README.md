# Circuits

OrCAD Capture / PSpice 工程入口说明。

> **克隆仓库后**：工程文件位于仓库根目录的 [`memristor/`](../memristor/)、[`memtest/`](../memtest/)。  
> 本地 Windows 开发环境可通过 junction 将本目录链接至上述文件夹；GitHub 上请直接打开 `memtest/` 路径。

| 路径 | 内容 |
|------|------|
| [`../memristor/`](../memristor/) | AIST 忆阻模型、`mem.opj` 基础单元（SJ/NAL/EN） |
| [`../memtest/`](../memtest/) | 系统级仿真：MMAM、语义饱和、痛觉测试等 |
| [`experimental/`](experimental/) | 新奇度通路说明 → 工程见 [`../memtest/somethingnew/`](../memtest/somethingnew/) |

## 推荐打开顺序

1. `memristor/zy_memristor/memristor_zhang.lib` — 忆阻 SPICE 子电路
2. `memtest/MMAM design/MMAM.opj` — 三通道完整系统
3. `memtest/yuyibaohe/SemanticSatiation.opj` — 语义饱和双通道
4. `memtest/somethingnew/saikai.opj` — 新奇度通路（探索性）

## 仿真输出说明

PSpice 运行后生成的 `*-PSpiceFiles/` 与 `*.dat` 体积可达数 GB，**不纳入 Git**。克隆后请在本地运行仿真重新生成；波形 CSV 见 [`simulation/data/`](../simulation/data/)（超大文件见 `.gitignore`，需自行导出）。

## 关键网表信号（MMAM）

- `EC1/EC2/EC3` — 共存检测子电路
- `AndEC12/13/23` — 方向性门控
- `M12, M21, M13, M31, M23, M32` — 方向性联想忆阻
- `VR1/VR2/VR3` — 检索巡回信号
- `VM1/VM2/VM3` — 通道使能/生理响应
