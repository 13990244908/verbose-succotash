"""
《统计与数据分析》Python 基础 03：表达式

学习目标：
  1. 分清表达式（有值）和语句（做动作），知道哪里能写表达式。
  2. 认识各种字面量写法，包括数字分隔符与科学计数法。
  3. 会用三元条件表达式和海象运算符 `:=` 精简代码。
  4. 掌握列表/字典/集合推导式，一行生成新数据。
  5. 会用 sum / max / sorted / zip / enumerate 等常用内置函数。
  6. 避开「别名陷阱」——两个名字指向同一个列表时的连带修改。

运行方法：
  在 VSCode 里打开本文件，点右上角 ▶ Run Python File，或按 Ctrl + F5；
  或在命令行执行：python 03_expressions.py

提示：文件末尾有练习与参考答案。想先自己做，就把「参考答案」那一段注释掉再运行。
"""

# ==== 1. 表达式与语句 ====
# 为什么：函数参数、推导式、lambda 里只能写表达式，写语句会报错。
# 是什么：表达式会被求值并产生一个值；语句是执行一个动作，本身没有值。
ctr = 360 / 12000          # 右边 360 / 12000 是表达式；整行 `ctr = ...` 是赋值语句
print(ctr)                 # -> 0.03
print(360 / 12000)         # -> 0.03（表达式可以直接塞进 print）

# 表达式能放在等号右边、函数参数里
print(round(360 / 12000, 4))            # -> 0.03
print("点击率", f"{360 / 12000:.2%}")    # -> 点击率 3.00%

# 语句不能当值用（下面两行取消注释都会报 SyntaxError）
# x = (if ctr > 0.02: print("好"))       # if 是语句，不能放进表达式
# print((a = 5))                         # 赋值是语句（海象运算符 := 例外，见第 4 节）

# 【动手改】把 print(360 / 12000) 改成 print(360 // 12000)，看整数除法的结果。


# ==== 2. 字面量 ====
# 为什么：数字一大就数不清位数，用分隔符和指数写法能少写错几个零。
# 是什么：字面量就是直接写出来的值，Python 按写法推断它的类型。
impressions = 1_200_000                 # 下划线分隔，等价 1200000，只是更好读
budget = 1.5e4                          # 科学计数法，等价 15000.0
ratio = 0.032
name = "夏季促销"                        # 字符串
is_ok = True                            # 布尔
empty = None                            # 空值

print(impressions, type(impressions).__name__)   # -> 1200000 int
print(budget, type(budget).__name__)             # -> 15000.0 float
print(f"{ratio}, {name}, {is_ok}, {empty}")      # -> 0.032, 夏季促销, True, None

# 字符串也有多种写法
print('单引号')                           # -> 单引号
print("双引号")                           # -> 双引号
print("含'引号'的字符串")                  # -> 含'引号'的字符串
print("换行\t制表")                       # 转义字符

# 【动手改】把 1_200_000 的下划线去掉再运行，看值是否相同。


# ==== 3. 条件表达式（三元）====
# 为什么：根据条件二选一赋值，写四行 if/else 太啰嗦。
# 是什么：`A if 条件 else B`——条件为真取 A，否则取 B。它本身是个表达式。
ctr = 0.032
status = "达标" if ctr >= 0.03 else "未达标"
print(status)                           # -> 达标

ctr = 0.018
print("达标" if ctr >= 0.03 else "未达标")   # -> 未达标

# 可以嵌套，但嵌套两层以上就该改用 if/elif，否则难读
level = "优" if ctr >= 0.05 else ("良" if ctr >= 0.03 else "待优化")
print(level)                            # -> 待优化

# 给可能是 None 的值兜底
cost = None
print(cost if cost is not None else 0)  # -> 0

# 【动手改】把 ctr 改成 0.06，看 level 变成什么。


# ==== 4. 海象运算符 := ====
# 为什么：想在判断的同时把中间结果存下来，用它可以少算一次、少写一行。
# 是什么：`变量 := 表达式` 能在表达式内部完成赋值（Python 3.8+）。
channels = ["搜索", "信息流", "开屏", "激励视频"]
if (count := len(channels)) > 3:
    print(f"渠道较多，共 {count} 个")      # -> 渠道较多，共 4 个

# 不用海象就得写两遍或先算一次
n = len(channels)
if n > 3:
    print(f"（对照）同样是 {n} 个")        # -> （对照）同样是 4 个

# 在 while 里也常用（这里用固定次数演示，避免读键盘输入）
total, i = 0, 0
while (i := i + 1) <= 5:
    total += i
print("1 到 5 的和:", total)              # -> 15

# 【动手改】把 > 3 改成 > 5，看 if 分支是否还会执行。


# ==== 5. 推导式 ====
# 为什么：把一组数据变成另一组数据，推导式一行搞定，比循环更清楚。
# 是什么：`[新元素 for 元素 in 可迭代对象 if 条件]`，列表/字典/集合都有。
ctrs = [0.032, 0.028, 0.041, 0.019]

# 列表推导：全部转成百分比
print([c * 100 for c in ctrs])
# -> [3.2, 2.8000000000000003, 4.1000000000000005, 1.9]（浮点误差，见 02 号文件）
print([round(c * 100, 1) for c in ctrs])          # -> [3.2, 2.8, 4.1, 1.9]（推荐写法）
# 带条件：只要达标的
print([c for c in ctrs if c >= 0.03])             # -> [0.032, 0.041]
# 带三元：转成评价
print(["达标" if c >= 0.03 else "未达标" for c in ctrs])
# -> ['达标', '未达标', '达标', '未达标']

# 字典推导：渠道 -> 曝光
pairs = [("搜索", 12000), ("信息流", 8000)]
print({k: v for k, v in pairs})                   # -> {'搜索': 12000, '信息流': 8000}
# 键值互换
print({v: k for k, v in pairs})                   # -> {12000: '搜索', 8000: '信息流'}

# 集合推导：自动去重
print({round(c, 3) for c in [0.032, 0.032, 0.041, 0.041]})   # -> {0.032, 0.041}

# 【动手改】把 `c >= 0.03` 改成 `c >= 0.04`，看筛出来几个。


# ==== 6. 常用内置函数 ====
# 为什么：统计指标基本就靠这几个函数，不必自己写循环。
# 是什么：Python 自带的现成函数，直接调用即可。
impressions_list = [12000, 8000, 5000, 15000]

print("len:", len(impressions_list))              # -> 4
print("sum:", sum(impressions_list))              # -> 40000
print("max / min:", max(impressions_list), min(impressions_list))   # -> 15000 5000
print("mean:", sum(impressions_list) / len(impressions_list))       # -> 10000.0
print("sorted:", sorted(impressions_list))        # -> [5000, 8000, 12000, 15000]
print("降序:", sorted(impressions_list, reverse=True))  # -> [15000, 12000, 8000, 5000]
print("abs:", abs(-3.5), "round:", round(3.14159, 2))   # -> 3.5 3.14

# enumerate：同时拿下标和值
for i, ch in enumerate(["搜索", "信息流"]):
    print(f"  {i}: {ch}")
# -> 0: 搜索 / 1: 信息流

# zip：把两组数据配对
for ch, imp in zip(["搜索", "信息流"], [12000, 8000]):
    print(f"  {ch}: {imp}")
# -> 搜索: 12000 / 信息流: 8000

# any / all：有没有一个达标 / 是不是全部达标
print("有达标:", any(c >= 0.03 for c in ctrs))     # -> True
print("全达标:", all(c >= 0.03 for c in ctrs))     # -> False

# 【动手改】把 all 的条件改成 c > 0，看是否变成 True。


# ==== 7. 别名陷阱 ====
# 为什么：两个名字指向同一个列表时，改一个另一个也变——数据分析里最容易踩。
# 是什么：`b = a` 不复制数据，只是让 b 也指向 a 那个对象。
channels_a = ["搜索", "信息流"]
channels_b = channels_a              # 不是复制，是别名
channels_b.append("开屏")
print("channels_a:", channels_a)     # -> ['搜索', '信息流', '开屏']（a 也被改了！）
print("是同一对象:", channels_a is channels_b)   # -> True

# 正确的复制方式（浅拷贝）
src = ["搜索", "信息流"]
copy1 = src.copy()
copy2 = src[:]
copy3 = list(src)
copy1.append("开屏")
print("src 不受影响:", src)           # -> ['搜索', '信息流']
print("copy1:", copy1)               # -> ['搜索', '信息流', '开屏']

# 嵌套结构要用深拷贝
import copy as copy_module
nested = [["搜索"], ["信息流"]]
deep = copy_module.deepcopy(nested)
deep[0].append("开屏")
print("nested 不受影响:", nested)     # -> [['搜索'], ['信息流']]

# 【动手改】把 channels_b = channels_a 改成 channels_b = channels_a.copy()，看 a 是否还被改。


# ==== 8. 求值顺序 ====
# 为什么：表达式里有多个函数调用时，执行先后会影响结果（尤其带副作用的操作）。
# 是什么：Python 从左到右求值；赋值语句先算完右边，再赋给左边。
def note(x):
    print(f"  求值为 {x}", end=" ")
    return x

print("从左到右:")
result = note(1) + note(2) + note(3)
print("\n  合计:", result)            # -> 合计: 6

# 赋值先算右边
nums = [1, 2, 3]
nums = nums + [4]
print("重新赋值后:", nums)            # -> [1, 2, 3, 4]

# 链式比较是「与」的简写，中间值只算一次
x = 5
print("1 < x < 10:", 1 < x < 10)      # -> True（等价 1 < x and x < 10）

# and / or 短路（见 02 号文件第 3 节）也是求值顺序的一部分
print("短路:", 0 and note(99))         # -> 0（右边根本没执行）

# 【动手改】把 note(1) + note(2) 换成 note(2) + note(1)，看打印顺序如何变化。


# ===== 练习 =====
# 1. 用三元表达式判断 ctr = 0.025 是否达标（>= 0.03），输出「达标」或「未达标」。
#    验证方式：输出「未达标」
# 2. 用列表推导把 [12000, 8000, 5000] 中大于 6000 的曝光量筛出来。
#    验证方式：[12000, 8000]
# 3. 用 sum / len 算出 [0.032, 0.028, 0.041] 的平均点击率（保留四位小数）。
#    验证方式：0.0337
# 4. 复制列表 ["搜索", "信息流"] 并追加 "开屏"，确认原列表没被改动。
#    验证方式：原列表仍是 ['搜索', '信息流']

# ===== 参考答案 =====
print("\n--- 参考答案 ---")

# 1
ctr = 0.025
print("1.", "达标" if ctr >= 0.03 else "未达标")          # -> 未达标

# 2
print("2.", [v for v in [12000, 8000, 5000] if v > 6000])  # -> [12000, 8000]

# 3
ctrs = [0.032, 0.028, 0.041]
print("3.", round(sum(ctrs) / len(ctrs), 4))              # -> 0.0337

# 4
original = ["搜索", "信息流"]
copied = original.copy()
copied.append("开屏")
print("4. 原列表:", original, "| 副本:", copied)
# -> 原列表: ['搜索', '信息流'] | 副本: ['搜索', '信息流', '开屏']
