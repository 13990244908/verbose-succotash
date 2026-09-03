# -*- coding: utf-8 -*-
"""第 4 章 示例代码：概率与常见分布

用法：
    python chapters/ch04_code.py
"""
import matplotlib

matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
matplotlib.rcParams["axes.unicode_minus"] = False

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm

print("=" * 60)
print("第 4 章  概率与常见分布")
print("=" * 60)

# 1. 二项分布
print("\n【1】二项分布：抛 10 次硬币，正面次数")
print("恰好 6 次正面的概率：", round(binom.pmf(6, n=10, p=0.5), 4))
print("不超过 6 次正面的概率：", round(binom.cdf(6, n=10, p=0.5), 4))

# 2. 正态分布概率密度
print("\n【2】正态分布")
x = np.linspace(-4, 4, 500)
y = norm.pdf(x, loc=0, scale=1)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="steelblue", lw=2)
plt.fill_between(x, y, where=(x >= -1.96) & (x <= 1.96), color="orange", alpha=0.4)
plt.title("标准正态分布（橙色区域约 95%）")
plt.xlabel("取值")
plt.ylabel("概率密度")
plt.savefig("chapters/fig_normal.png", dpi=150)
print("已保存：chapters/fig_normal.png")

# 3. 68-95-99.7 法则验证
print("\n【3】验证 68-95-99.7 法则（标准正态）")
for k in (1, 2, 3):
    p = norm.cdf(k) - norm.cdf(-k)
    print(f"落在 μ ± {k}σ 内的概率：{p:.4f}")

# 4. 累积概率计算
print("\n【4】累积概率")
print("小于 1.96 的概率：", round(norm.cdf(1.96), 4))
print("大于 1.96 的概率：", round(1 - norm.cdf(1.96), 4))

# 5. 模拟：大量随机变量均值的分布趋近正态（中心极限定理的直观感受）
print("\n【5】中心极限定理直观演示")
rng = np.random.default_rng(42)
means = []
for _ in range(2000):
    # 每次抽 30 个 0~1 均匀分布的数，取均值
    sample = rng.uniform(0, 1, 30)
    means.append(sample.mean())

plt.figure(figsize=(8, 5))
plt.hist(means, bins=40, color="lightgreen", edgecolor="black", density=True)
plt.title("2000 次「30 个均匀随机数均值」的分布（趋近正态）")
plt.xlabel("样本均值")
plt.ylabel("密度")
plt.savefig("chapters/fig_clt.png", dpi=150)
print("已保存：chapters/fig_clt.png（可见均值分布已趋近钟形）")
