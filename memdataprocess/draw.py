import pandas as pd
import matplotlib.pyplot as plt

# 大字号设置
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# 读取数据
df = pd.read_csv('yeharm.csv', skipinitialspace=True)
df.columns = df.columns.str.strip()

time = df['Time']
v_vr2 = df['V(VR3)']
v_vm2 = df['V(VM3)']

# 创建上下两个子图，共享 X 轴
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# 上图：V(VR1)
ax1.plot(time, v_vr2, color='#1E90FF', linewidth=1.5)
ax1.set_ylabel('V(VR3) (V)')
ax1.grid(True, linestyle='--', alpha=0.7)

# 下图：V(VM1)
ax2.plot(time, v_vm2, color='#1E90FF', linewidth=1.5)
ax2.set_ylabel('V(VM3) (V)')
ax2.set_xlabel('Time (s)')
ax2.grid(True, linestyle='--', alpha=0.7)

# 调整子图间距
plt.tight_layout()
plt.show()