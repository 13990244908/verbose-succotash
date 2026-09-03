# 统计数据分析（Statistics Data Analysis）

一门面向**本科入门**同学的统计数据分析课程，用 **Python** 语言，从零开始讲解统计概念，并配合可运行的代码和示例数据，帮助你把「统计知识」和「编程实践」结合起来。

> 定位：零基础 / 文科背景也能跟上。每个概念都从直觉讲起，代码从最基础开始。

---

## 目录

| 章节 | 主题 | 核心内容 |
| --- | --- | --- |
| 第 1 章 | 数据分析与 Python 入门 | 分析流程、Python 基础、NumPy/Pandas 初识 |
| 第 2 章 | 描述统计 | 均值/中位数/众数、方差/标准差、四分位数 |
| 第 3 章 | 数据可视化 | 直方图、箱线图、散点图、折线图 |
| 第 4 章 | 概率与常见分布 | 概率、随机变量、正态分布、二项分布 |
| 第 5 章 | 统计推断 | 抽样分布、中心极限定理、置信区间 |
| 第 6 章 | 假设检验 | 原假设、p 值、t 检验、卡方检验 |

每章都包含：
- **讲义**（`chapters/ch0X-*.md`）：概念讲解 + 图文说明
- **代码**（`chapters/ch0X_code.py`）：可直接运行的 Python 脚本
- **练习**（`exercises/`）：章节末尾的思考题与编程题

---

## 环境准备

本课程需要 **Python 3.10 及以上**，并安装以下依赖：

```bash
pip install -r requirements.txt
```

依赖清单：`numpy`、`pandas`、`matplotlib`、`scipy`。

> 国内用户可在 pip 命令后追加清华镜像加速：
> `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 快速开始

1. 克隆本仓库：
   ```bash
   git clone https://github.com/你的用户名/statistics-data-analysis.git
   cd statistics-data-analysis
   ```
2. 安装依赖（见上）。
3. 生成示例数据（只需一次）：
   ```bash
   python generate_data.py
   ```
4. 按章节顺序运行代码：
   ```bash
   python chapters/ch01_code.py
   python chapters/ch02_code.py
   # ...
   ```

---

## 目录结构

```
statistics-data-analysis/
├── README.md              # 本文件：课程总览与使用说明
├── requirements.txt       # Python 依赖清单
├── generate_data.py       # 示例数据生成脚本（可复现）
├── data/                  # 示例数据集（运行 generate_data.py 生成）
│   ├── students.csv       # 学生成绩数据
│   └── sales.csv          # 销售数据
├── chapters/              # 每章讲义 + 代码
│   ├── ch01-数据分析与Python入门.md
│   ├── ch01_code.py
│   ├── ...
└── exercises/             # 练习题
    └── 练习题.md
```

---

## 示例数据说明

- `students.csv`：200 名学生的成绩数据，字段为 `学号、性别、专业、数学、英语、编程`。
- `sales.csv`：某店铺 60 天的销售记录，字段为 `日期、品类、销售额、销量`。

数据由 `generate_data.py` 用固定随机种子生成，保证每次生成结果一致、可复现。

---

## 许可证

MIT License
