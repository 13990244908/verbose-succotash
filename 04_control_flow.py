"""
《统计与数据分析》Python 基础 04：流程控制

学习目标：
  1. 理解缩进就是 Python 的语法，不是排版习惯。
  2. 掌握 if / elif / else，并记住哪些值会被当成「假」。
  3. 会用 while、for + range 处理重复任务。
  4. 掌握 break、continue 和循环 else 的执行时机。
  5. 会写嵌套循环，并避开「遍历时改列表」「闭包延迟绑定」这两个坑。
  6. 了解 match / case 多分支匹配（Python 3.10+）。

运行方法：
  在 VSCode 里打开本文件，点右上角 ▶ Run Python File，或按 Ctrl + F5；
  或在命令行执行：python 04_control_flow.py

提示：文件末尾有练习与参考答案。想先自己做，就把「参考答案」那一段注释掉再运行。
"""

# ==== 1. 缩进即语法 ====
# 为什么：别的语言用花括号分块，Python 用缩进——缩进错了代码逻辑就错了。
# 是什么：同一层代码必须对齐；通常一层缩进 = 4 个空格。
ctr = 0.032
if ctr >= 0.03:
    print("达标")          # 缩进 4 空格，属于 if 块
    print("继续保持")      # 同样缩进，还是 if 块
print("这一行不属于 if")    # 无缩进，if 结束了，无论如何都会执行

# 缩进不一致会直接报错 IndentationError
# if ctr > 0:
#     print("a")
#       print("b")         # IndentationError: unexpected indent

# 建议：在 VSCode 右下角把缩进设为「空格: 4」，别混用 Tab 和空格

# 【动手改】把 ctr 改成 0.01，看 if 块里的两行是否还会打印。


# ==== 2. if / elif / else 与假值清单 ====
# 为什么：判断「预算是否超支」「渠道是否达标」都靠它；而「假值」不止 False。
# 是什么：从上往下逐个判断条件，命中第一个为真就执行并跳出整个分支。
ctr = 0.041
if ctr >= 0.05:
    level = "优"
elif ctr >= 0.03:
    level = "良"
elif ctr >= 0.01:
    level = "一般"
else:
    level = "待优化"
print(f"点击率 {ctr:.1%} -> {level}")      # -> 点击率 4.1% -> 良

# 假值清单：下面这些在 if 判断里都等价于 False
falsy = [False, 0, 0.0, "", [], {}, set(), None]
for v in falsy:
    print(f"  {str(v):<8} -> bool: {bool(v)}")
# -> 全部是 False（注意：0、空字符串、空列表、None 都是假）

# 判断 None 要显式，别让 0 被误判
clicks = 0
if clicks is None:
    print("  数据缺失")
elif clicks == 0:
    print("  真的没有点击")                  # -> 真的没有点击

# 【动手改】把 falsy 里的 0 换成 "0"（字符串），看 bool 变成什么。


# ==== 3. while 循环 ====
# 为什么：不知道要循环多少次，只知道「到此为止」的条件时用它。
# 是什么：条件为真就反复执行；务必保证条件最终会变成假，否则死循环。
budget, spent = 10000, 0
day = 0
while spent < budget:
    spent += 1500
    day += 1
print(f"第 {day} 天预算耗尽，累计花费 {spent}")   # -> 第 7 天预算耗尽，累计花费 10500

# while True + break 的写法（条件写在中间，更灵活）
total = 0
while True:
    total += 1
    if total >= 5:
        break
print("累加到:", total)                        # -> 5

# 【动手改】把 spent += 1500 改成 spent += 500，看需要多少天。


# ==== 4. for 循环与 range ====
# 为什么：遍历一组数据是数据分析最常见的动作。
# 是什么：for 依次取出可迭代对象里的元素；range 生成一串整数。
channels = ["搜索", "信息流", "开屏"]
for ch in channels:
    print(f"  渠道: {ch}")
# -> 搜索 / 信息流 / 开屏

print("range(3):", list(range(3)))             # -> [0, 1, 2]
print("range(1, 4):", list(range(1, 4)))       # -> [1, 2, 3]
print("range(0, 10, 2):", list(range(0, 10, 2)))   # -> [0, 2, 4, 6, 8]
print("倒着数:", list(range(5, 0, -1)))         # -> [5, 4, 3, 2, 1]

# 需要下标时用 enumerate（见 03 号文件）
for i, ch in enumerate(channels):
    print(f"  {i}: {ch}")
# -> 0: 搜索 / 1: 信息流 / 2: 开屏

# 遍历字典
kpi = {"ctr": 0.032, "cvr": 0.015}
for key, value in kpi.items():
    print(f"  {key} = {value}")
# -> ctr = 0.032 / cvr = 0.015

# 【动手改】把 range(0, 10, 2) 改成 range(0, 10, 3)，看步长变化。


# ==== 5. break 与 continue ====
# 为什么：找到目标就不用再找了（break）；某些数据要跳过（continue）。
# 是什么：break 直接结束整个循环；continue 跳过本轮，进入下一轮。
ctrs = [0.021, 0.028, 0.041, 0.052]

for c in ctrs:
    if c >= 0.04:
        print(f"  第一个达标的是 {c:.1%}")     # -> 第一个达标的是 4.1%
        break

print("跳过低点击率，只看达标的:")
for c in ctrs:
    if c < 0.03:
        continue
    print(f"  {c:.1%} 达标")
# -> 4.1% 达标 / 5.2% 达标（0.021 和 0.028 被 continue 跳过）

# 注意：for 循环里改 range 的次数不影响循环次数
for i in range(3):
    i = 100        # 改的是变量 i，下一次循环会被重新赋值
    print("  i =", i)
# -> 100 100 100（但循环仍执行 3 次）

# 【动手改】把 break 换成 continue，看输出有什么不同。


# ==== 6. 循环 else ====
# 为什么：想区分「循环正常跑完」和「中途 break 掉」——这正是 else 的用处。
# 是什么：循环没被 break 中断时，else 块会执行。
def find_channel(target, channels):
    for ch in channels:
        if ch == target:
            print(f"  找到了 {ch}")
            break
    else:
        print(f"  没有找到 {target}")

find_channel("开屏", ["搜索", "信息流", "开屏"])     # -> 找到了 开屏
find_channel("视频", ["搜索", "信息流", "开屏"])     # -> 没有找到 视频

# 典型用法：检查是否全部达标
ctrs_all_ok = [0.032, 0.041, 0.055]
for c in ctrs_all_ok:
    if c < 0.03:
        print("  有未达标的渠道")
        break
else:
    print("  全部渠道达标")                      # -> 全部渠道达标

# 【动手改】往 ctrs_all_ok 里加一个 0.01，看 else 还会不会执行。


# ==== 7. 嵌套循环 ====
# 为什么：渠道 × 日期、行 × 列这类二维数据要两层循环。
# 是什么：外层走一步，内层走完整一圈。
channels = ["搜索", "信息流"]
days = ["周一", "周二"]

for ch in channels:
    for day in days:
        print(f"  {ch} - {day}")
# -> 搜索-周一 / 搜索-周二 / 信息流-周一 / 信息流-周二

# 用嵌套循环算总和
matrix = [[12000, 8000], [5000, 3000]]
total_impressions = 0
for row in matrix:
    for value in row:
        total_impressions += value
print("总曝光:", total_impressions)              # -> 28000

# 同样的结果，用 sum + 推导式更简洁
print("用推导式:", sum(sum(row) for row in matrix))   # -> 28000

# 【动手改】把 matrix 加一行，看总曝光变化。


# ==== 8. 循环变量的坑 ====
# 为什么：这两个坑都很隐蔽——代码能跑，但结果不对。
# 是什么：① 遍历时别增删列表；② 循环里定义的函数会在调用时才取变量值。

# 坑一：边遍历边删，会漏掉元素
numbers = [1, 2, 3, 4, 5]
for n in numbers[:]:                 # 遍历副本，才能安全地改原列表
    if n % 2 == 0:
        numbers.remove(n)
print("删除偶数后:", numbers)          # -> [1, 3, 5]

# 更推荐：用推导式生成新列表
numbers2 = [1, 2, 3, 4, 5]
print("用推导式:", [n for n in numbers2 if n % 2 != 0])   # -> [1, 3, 5]

# 坑二：闭包延迟绑定——函数记住的是变量，不是当时的值
funcs = [lambda: i for i in range(3)]
print("延迟绑定:", [f() for f in funcs])         # -> [2, 2, 2]（不是 0,1,2）

# 修正：用默认参数把当前值「钉」住
funcs_fixed = [lambda i=i: i for i in range(3)]
print("修正后:", [f() for f in funcs_fixed])     # -> [0, 1, 2]

# 【动手改】把 numbers[:] 改成 numbers，看删除结果是否完整。


# ==== 9. match / case ====
# 为什么：按某个值的不同取值走不同分支时，比一长串 if/elif 清楚。
# 是什么：Python 3.10+ 的模式匹配，类似其他语言的 switch。
def suggest(channel):
    match channel:
        case "搜索":
            return "意图明确，提高出价"
        case "信息流" | "开屏":      # 用 | 匹配多个值
            return "曝光为主，控频次"
        case _:                     # 默认分支，必须放最后
            return "未知渠道，先小量测试"

for ch in ["搜索", "信息流", "视频"]:
    print(f"  {ch}: {suggest(ch)}")
# -> 搜索: 意图明确，提高出价 / 信息流: 曝光为主，控频次 / 视频: 未知渠道，先小量测试

# 【动手改】在 case "信息流" | "开屏" 里加一个 "激励视频"，看输出变化。


# ===== 练习 =====
# 1. 用 if/elif/else 给点击率分级：>=5% 优、>=3% 良、>=1% 一般，其余待优化。
#    给 ctr = 0.042 分级。验证方式：输出「良」
# 2. 用 for + range 计算 1 到 100 中所有能被 7 整除的数之和。
#    验证方式：735
# 3. 用 break 找出 [0.021, 0.028, 0.041, 0.052] 中第一个 >= 0.04 的值。
#    验证方式：0.041
# 4. 用嵌套循环算 [[1, 2], [3, 4]] 的所有元素之和。
#    验证方式：10

# ===== 参考答案 =====
print("\n--- 参考答案 ---")

# 1
ctr = 0.042
if ctr >= 0.05:
    grade = "优"
elif ctr >= 0.03:
    grade = "良"
elif ctr >= 0.01:
    grade = "一般"
else:
    grade = "待优化"
print("1.", grade)                               # -> 良

# 2
total = sum(n for n in range(1, 101) if n % 7 == 0)
print("2.", total)                               # -> 735

# 3
for c in [0.021, 0.028, 0.041, 0.052]:
    if c >= 0.04:
        print("3.", c)                           # -> 0.041
        break

# 4
matrix = [[1, 2], [3, 4]]
total = 0
for row in matrix:
    for v in row:
        total += v
print("4.", total)                               # -> 10
