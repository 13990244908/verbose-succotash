"""
《统计与数据分析》Python 基础 02：运算符

学习目标：
  1. 掌握算术运算符，尤其是 `/`、`//`、`%` 的取整与符号规则。
  2. 知道浮点数有误差，比较小数不能直接用 `==`。
  3. 理解 `and` / `or` 会短路，而且返回的是操作数本身而不是 True/False。
  4. 分清 `in`（在不在里面）与 `is`（是不是同一个对象）。
  5. 了解位运算与运算符优先级。

运行方法：
  在 VSCode 里打开本文件，点右上角 ▶ Run Python File，或按 Ctrl + F5；
  或在命令行执行：python 02_operators.py

提示：文件末尾有练习与参考答案。想先自己做，就把「参考答案」那一段注释掉再运行。
"""

import math  # 标准库，提供 isclose() 用于安全地比较小数

# ==== 1. 算术运算符：取整与符号规则 ====
# 为什么：算 CPM、人均成本、分页时都要取整，取整方向错了结果就偏了。
# 是什么：`/` 永远得 float；`//` 向下取整（往数轴更小的方向）；`%` 取余，符号跟除数走。
impressions, clicks, cost = 12000, 360, 890.5

print("CPM（千次曝光成本）:", cost / impressions * 1000)   # -> 74.20833333333333
print("人均点击:", clicks / 7)                            # -> 51.42857142857143
print("7 / 2 =", 7 / 2)                                  # -> 3.5（/ 一定得小数）
print("7 // 2 =", 7 // 2)                                # -> 3（向下取整）
print("-7 // 2 =", -7 // 2)                              # -> -4（注意：不是 -3）
print("7 // -2 =", 7 // -2)                              # -> -4（往更小的方向取）
print("2 ** 10 =", 2 ** 10)                              # -> 1024（幂运算）

print("7 % 2 =", 7 % 2)                                  # -> 1
print("-7 % 2 =", -7 % 2)                                # -> 1（余数符号跟除数 2，为正）
print("判断能否整除:", 12000 % 4 == 0)                     # -> True

# 取整三兄弟的差别：// 向下、int() 向 0、round() 四舍五入
print(int(-3.7), round(-3.7), -3.7 // 1)                 # -> -3 -4 -4.0

# 【动手改】把 -7 // 2 改成 -7 / 2，看结果从 -4 变成 -3.5。


# ==== 2. 比较运算符与浮点误差 ====
# 为什么：判断「预算是否超支」「点击率是否达标」都要比较，而小数比较有陷阱。
# 是什么：比较得 bool。但二进制无法精确表示 0.1，累加后会有微小误差。
print("0.1 + 0.2 =", 0.1 + 0.2)                          # -> 0.30000000000000004
print("0.1 + 0.2 == 0.3 吗:", 0.1 + 0.2 == 0.3)          # -> False（坑！）
print("用 math.isclose:", math.isclose(0.1 + 0.2, 0.3))  # -> True（正确做法）

ctr = 0.030000000000000002
print("ctr == 0.03 吗:", ctr == 0.03)                    # -> 可能 False
print("安全写法:", math.isclose(ctr, 0.03))               # -> True

budget, spent = 10000, 10250.5
print("是否超支:", spent > budget)                        # -> True
print("差额:", round(spent - budget, 2))                  # -> 250.5

# 链式比较，比 and 更直观
score = 85
print("60 <= score <= 100:", 60 <= score <= 100)         # -> True

# 【动手改】把 0.1 + 0.2 换成 0.1 * 3，看是否也出现误差。


# ==== 3. and / or 的短路与返回值 ====
# 为什么：写默认值、做条件判断时，理解返回值能少写很多 if。
# 是什么：`and` / `or` 不一定返回 True/False，而是返回某个操作数；且会短路求值。
print("0 or '默认渠道':", 0 or "默认渠道")                 # -> 默认渠道
print("'搜索' and 100:", "搜索" and 100)                 # -> 100
print("'' or [] or '兜底':", "" or [] or "兜底")          # -> 兜底

# 短路：and 遇到假值就不再算右边，所以下面的除零不会发生
print("0 and 1/0:", 0 and 1 / 0)                        # -> 0（没报错）
# print(1 and 1 / 0)                                    # ZeroDivisionError

# 用 or 给可能是 None 的值兜底
channel = None
print("实际渠道:", channel or "未指定")                    # -> 未指定

# 注意：or 会把 0 和 "" 也当假值，想保留 0 要显式判断
clicks = 0
print("点击数:", clicks or "无数据")                       # -> 无数据（0 被当成假）

# 【动手改】把 clicks 改成 5，看输出变成什么。


# ==== 4. 赋值运算符 ====
# 为什么：累加曝光、累减预算这类操作，写 `+=` 更简洁。
# 是什么：`x += n` 等价于 `x = x + n`，其余同理。
total_cost = 0
total_cost += 890.5
total_cost += 210.0
print("累计成本:", total_cost)                            # -> 1100.5

impressions = 12000
impressions //= 1000
print("折算成千次:", impressions)                          # -> 12

ctr = 0.03
ctr *= 100
print("转成百分数:", ctr)                                 # -> 3.0

# 注意：+= 对 list 是原地追加，不是新建列表（区别见 01 号文件第 6 节）
channels = ["搜索"]
channels += ["信息流"]
print(channels)                                          # -> ['搜索', '信息流']

# 【动手改】把 ctr *= 100 改成 ctr **= 2，看结果变化。


# ==== 5. in 与 is ====
# 为什么：判断「渠道在不在名单里」和「是不是同一个对象」是两回事，混用会出隐蔽 bug。
# 是什么：`in` 检查成员关系（值在不在）；`is` 检查身份（是不是同一个对象）。
channels = ["搜索", "信息流", "开屏"]
print("'搜索' in channels:", "搜索" in channels)           # -> True
print("'视频' not in channels:", "视频" not in channels)   # -> True

list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("list_a == list_b:", list_a == list_b)              # -> True（值相等）
print("list_a is list_b:", list_a is list_b)              # -> False（不同对象）
list_c = list_a
print("list_a is list_c:", list_a is list_c)              # -> True（同一对象）

# 判断是否为 None，请用 is
result = None
print("result is None:", result is None)                  # -> True（推荐写法）
print("result == None:", result == None)                  # -> True（不推荐）

print("结论：比较值用 ==，判断 None 用 is，其余情况别用 is")

# 【动手改】把 list_b = [1, 2, 3] 改成 list_b = list_a，再看 is 的结果。


# ==== 6. 位运算 ====
# 为什么：多个开关状态压进一个整数（比如投放渠道组合），位运算最省空间。
# 是什么：把数当二进制位来操作：& 与、| 或、^ 异或、~ 取反、<< 左移、>> 右移。
SEARCH, FEED, SPLASH = 1, 2, 4        # 三种渠道各占一个二进制位

plan = SEARCH | SPLASH                # 投放搜索 + 开屏
print("plan =", plan, "二进制:", bin(plan))                # -> 5 0b101
print("是否投搜索:", (plan & SEARCH) != 0)                 # -> True
print("是否投信息流:", (plan & FEED) != 0)                 # -> False

print("5 & 1 =", 5 & 1)                                  # -> 1
print("5 | 2 =", 5 | 2)                                  # -> 7
print("5 ^ 1 =", 5 ^ 1)                                  # -> 4（异或：不同为 1）
print("1 << 3 =", 1 << 3)                                # -> 8（左移 3 位 = ×8）
print("16 >> 2 =", 16 >> 2)                              # -> 4（右移 2 位 = ÷4）

# 【动手改】把 plan 改成 SEARCH | FEED，看「是否投开屏」变成什么。


# ==== 7. 运算符优先级 ====
# 为什么：表达式一长，运算顺序就容易搞错，结果偏了还不知道为什么。
# 是什么：从高到低：** → 一元正负 → * / // % → + - → 比较 → not → and → or。
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)                # -> 50（先幂、再乘、后加）
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)            # -> 80（括号优先）
print("-2 ** 2 =", -2 ** 2)                              # -> -4（** 比负号优先）
print("(-2) ** 2 =", (-2) ** 2)                          # -> 4

print("not True or False =", not True or False)           # -> False
print("1 < 2 and 3 > 2 =", 1 < 2 and 3 > 2)              # -> True

# 算 CPM 时括号能避免歧义
cost, impressions = 890.5, 12000
cpm_wrong = cost / impressions * 1000
cpm_clear = (cost / impressions) * 1000
print("两种写法结果相同:", math.isclose(cpm_wrong, cpm_clear))   # -> True
print("建议：拿不准就加括号，可读性比省字符重要")

# 【动手改】把 2 + 3 * 4 ** 2 改成 (2 + 3 * 4) ** 2，看结果差多少。


# ===== 练习 =====
# 1. 有 12000 次曝光、360 次点击，算点击率并判断它是否达到 3% 的目标（用 >= 比较）。
#    验证方式：点击率 3.0%，达标 True
# 2. 判断 0.1 + 0.2 是否等于 0.3，再用 math.isclose 比较一次。
#    验证方式：第一次 False，第二次 True
# 3. 用 or 给变量 channel = "" 兜底，输出 "未指定"；再说明为什么 0 也会被替换掉。
#    验证方式：输出「未指定」
# 4. 用位运算表示「搜索 + 信息流」两种渠道，判断其中是否包含「开屏」。
#    验证方式：不包含，输出 False

# ===== 参考答案 =====
print("\n--- 参考答案 ---")

# 1
impressions, clicks = 12000, 360
ctr = clicks / impressions
print(f"1. 点击率 {ctr:.1%}，达标: {ctr >= 0.03}")         # -> 3.0%，达标: True

# 2
print("2. ==", 0.1 + 0.2 == 0.3, "| isclose:", math.isclose(0.1 + 0.2, 0.3))
# -> == False | isclose: True

# 3
channel = ""
print("3. 渠道:", channel or "未指定")                      # -> 未指定
print("   因为 0、''、[]、None 都是假值，or 会一路找到第一个真值")

# 4
SEARCH, FEED, SPLASH = 1, 2, 4
plan = SEARCH | FEED
print("4. 是否投开屏:", (plan & SPLASH) != 0)              # -> False
