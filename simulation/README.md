# Simulation

PSpice 波形导出 CSV 与 Python 后处理脚本。

## 数据

`data/` 目录包含从 PSpice 导出的 CSV（与 `memdataprocess/` 同步）。

**Git 体积控制：** 超过 100 MB 的文件（`noharm.csv`、`harmfulstmmalresult.csv`、`SS.csv`）已列入 `.gitignore`，需在本地从 PSpice 重新导出。其余 CSV 可直接用于 `draw.py` 绘图。

| 文件 | 场景 |
|------|------|
| `10.csv`–`40.csv` | 不同刺激强度 |
| `0.5V.csv`, `0.7V`, `1.0V.csv` | 电压扫描 |
| `yeharm.csv`, `noc0.2.csv`, `noc0.8.csv` | 有害/无害、痛觉感受器 |
| `EN.csv`, `TT.csv` | 编码神经元测试 |
| `noharm.csv` 等（本地生成） | 见 `.gitignore`，需自行导出 |

原始导出与 `memdataprocess/draw.py` 仍保留在 `memdataprocess/`（含 `.venv`，已 gitignore）。

## 脚本

```bash
pip install -r simulation/requirements.txt
python simulation/scripts/draw.py
python simulation/scripts/draw.py --csv simulation/data/noharm.csv
```

## 新增 CSV

在 OrCAD PSpice 中 Trace → Plot → Save to CSV，放入 `simulation/data/` 即可。
