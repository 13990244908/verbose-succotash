"""
《统计与数据分析》Python 基础 05：函数

学习目标：
  1. 会用 `def` 定义函数，理解 `return` 与「没有 return 时返回 None」。
  2. 分清位置参数、默认参数、关键字参数三种用法。
  3. 避开「可变默认参数」这个经典陷阱。
  4. 会用 `*args` / `**kwargs` 接收不定数量的参数。
  5. 理解多返回值与解包，以及 LEGB 作用域规则。
  6. 会写 lambda、docstring、类型注解，了解递归与函数作为参数。

运行方法：
  在 VSCode 里打开本文件，点右上角 ▶ Run Python File，或按 Ctrl + F5；
  或在命令行执行：python 05_functions.py

提示：文件末尾有练习与参考答案。想先自己做，就把「参考答案」那一段注释掉再运行。
"""

# ==== 1. def 与返回值 ====
# 为什么：同一段计算要反复用（算 CTR、CPM、ROI），写成函数就不用复制粘贴。
# 是什么：`def 名字(参数):` 定义函数，`return` 把结果交回调用处。
def calc_ctr(clicks, impressions):
    """点击率 = 点击 / 曝光"""
    return clicks / impressions

print(calc_ctr(360, 12000))          # -> 0.03

# 没有 return 的函数，实际返回 None
def log(msg):
    print("  [日志]", msg)

result = log("投放开始")
print("返回值:", result)              # -> None（print 只是副作用）

# return 后面的代码不会执行
def classify(ctr):
    if ctr >= 0.03:
        return "达标"
    return "未达标"
    # print("这里永远不会执行")

print(classify(0.041), classify(0.018))   # -> 达标 未达标

# 【动手改】把 calc_ctr 的 return 去掉，看 print(calc_ctr(...)) 输出什么。


# ==== 2. 三类参数 ====
# 为什么：参数灵活，一个函数才能应对不同场景。
# 是什么：位置参数按顺序传；默认参数可省略；关键字参数用 `名字=` 指定。
def report(channel, impressions, ctr_threshold=0.03, unit="%"):
    """输出渠道报告。ctr_threshold 和 unit 有默认值，可省略。"""
    return f"{channel}: 曝光 {impressions}，达标线 {ctr_threshold:.1%}（{unit}）"

print(report("搜索", 12000))                                  # 用默认阈值
# -> 搜索: 曝光 12000，达标线 3.0%（%）
print(report("信息流", 8000, 0.05))                            # 位置参数覆盖默认值
# -> 信息流: 曝光 8000，达标线 5.0%（%）
print(report("开屏", 5000, ctr_threshold=0.02, unit="百分比"))  # 关键字参数，顺序可换
# -> 开屏: 曝光 5000，达标线 2.0%（百分比）

# 注意：默认参数必须放在普通参数后面，否则 SyntaxError
# def bad(a=1, b): ...

# 【动手改】把 report("搜索", 12000) 改成 report(channel="搜索", impressions=12000)，看结果是否相同。


# ==== 3. 可变默认参数陷阱 ====
# 为什么：这是 Python 最经典的坑——默认的可变对象只在定义时创建一次，之后每次调用共用。
# 是什么：不要用 `[]`、`{}` 这类可变对象当默认值。
def add_channel_bad(ch, target=[]):      # 陷阱写法
    target.append(ch)
    return target

print("第一次:", add_channel_bad("搜索"))        # -> ['搜索']
print("第二次:", add_channel_bad("信息流"))      # -> ['搜索', '信息流']（不干净了！）

# 正确写法：默认用 None，函数里再新建
def add_channel_ok(ch, target=None):
    if target is None:
        target = []
    target.append(ch)
    return target

print("修正-第一次:", add_channel_ok("搜索"))     # -> ['搜索']
print("修正-第二次:", add_channel_ok("信息流"))   # -> ['信息流']

# 【动手改】把 add_channel_ok 的 `if target is None` 删掉，看会不会报错。


# ==== 4. *args 与 **kwargs ====
# 为什么：有时事先不知道要传几个参数（比如求任意多个渠道的曝光总和）。
# 是什么：`*args` 收多余的位置参数（元组）；`**kwargs` 收多余的关键字参数（字典）。
def total_impressions(*args):
    """把传入的所有曝光量相加"""
    return sum(args)

print(total_impressions(12000, 8000))              # -> 20000
print(total_impressions(12000, 8000, 5000))        # -> 25000

def build_report(channel, **kwargs):
    """把任意指标打包成字典"""
    return {"渠道": channel, **kwargs}

print(build_report("搜索", ctr=0.032, cpm=74.2))   # -> {'渠道': '搜索', 'ctr': 0.032, 'cpm': 74.2}

# 调用时用 * 拆包
nums = [12000, 8000]
print(total_impressions(*nums))                    # -> 20000（把列表拆成位置参数）

# 【动手改】给 total_impressions 再传一个值，看总和变化。


# ==== 5. 多返回值与解包 ====
# 为什么：一次算出多个指标（均值、最大、最小）时，返回多个值最方便。
# 是什么：Python 用逗号返回多个值，实际是返回元组，可直接解包。
def summarize(values):
    """返回最小值、最大值、平均值"""
    return min(values), max(values), sum(values) / len(values)

low, high, avg = summarize([0.021, 0.032, 0.041])
print(f"最低 {low:.1%}，最高 {high:.1%}，平均 {avg:.1%}")
# -> 最低 2.1%，最高 4.1%，平均 3.1%

print("返回的其实是元组:", summarize([1, 2, 3]))     # -> (1, 3, 2.0)

# 只关心部分结果时用下划线占位
low, _, _ = summarize([0.021, 0.032, 0.041])
print("只要最低:", low)                            # -> 0.021

# 【动手改】把 [0.021, 0.032, 0.041] 加一个 0.09，看最高值变化。


# ==== 6. LEGB 作用域 ====
# 为什么：函数里能不能改外部变量，取决于作用域规则——改错了会静默失败或报错。
# 是什么：查找顺序 Local（本函数）→ Enclosing（外层函数）→ Global（模块）→ Built-in（内置）。
threshold = 0.03          # G: 全局

def outer():
    bonus = 0.01          # E: 外层函数的局部变量
    def inner():
        ctr = 0.041       # L: 本函数的局部变量
        return ctr, bonus, threshold
    return inner()

print("L, E, G:", outer())                # -> (0.041, 0.01, 0.03)

# 想在函数里改全局变量，要用 global
counter = 0
def increment():
    global counter
    counter += 1

increment()
increment()
print("counter:", counter)                 # -> 2

# 想在嵌套函数里改外层变量，要用 nonlocal
def make_counter():
    count = 0
    def add():
        nonlocal count
        count += 1
        return count
    return add

c = make_counter()
print("nonlocal:", c(), c())               # -> 1 2

# 【动手改】把 increment 里的 global counter 删掉，看会不会报错（会：UnboundLocalError）。


# ==== 7. lambda 与高阶函数 ====
# 为什么：排序、筛选时只需要一行小逻辑，专门 def 一个函数太重。
# 是什么：`lambda 参数: 表达式`，只能写一个表达式（不能写语句）。
channels = [("搜索", 12000), ("信息流", 8000), ("开屏", 5000)]

# 按曝光量排序
print(sorted(channels, key=lambda x: x[1]))
# -> [('开屏', 5000), ('信息流', 8000), ('搜索', 12000)]

# 按渠道名长度排序
print(sorted(channels, key=lambda x: len(x[0])))

# filter / map（多数时候推导式更好读，见 03 号文件）
print(list(filter(lambda x: x[1] >= 8000, channels)))
print(list(map(lambda x: x[0], channels)))          # -> ['搜索', '信息流', '开屏']

# lambda 也能直接调用（不推荐，失去意义）
print((lambda a, b: a + b)(3, 5))                   # -> 8

# 【动手改】把 sorted 的 key 改成 lambda x: -x[1]，看排序方向。


# ==== 8. docstring 与类型注解 ====
# 为什么：别人（和三个月后的你）要靠它知道函数怎么用、传什么类型。
# 是什么：函数体第一行写三引号字符串就是 docstring；`参数: 类型` 和 `-> 类型` 是注解。
def calc_cpm(cost: float, impressions: int) -> float:
    """
    计算千次曝光成本 CPM。

    参数:
        cost: 花费金额（元）
        impressions: 曝光次数

    返回:
        每千次曝光的成本（元）
    """
    if impressions == 0:
        return 0.0
    return cost / impressions * 1000

print(calc_cpm(890.5, 12000))              # -> 74.20833333333333
print("文档:", calc_cpm.__doc__.strip().splitlines()[0])   # -> 计算千次曝光成本 CPM。
print("注解:", calc_cpm.__annotations__)   # -> {'cost': <class 'float'>, 'impressions': <class 'int'>, 'return': <class 'float'>}

# 注意：注解只是提示，Python 运行时不检查类型
# print(calc_cpm("890.5", 12000))
# -> TypeError: 字符串不能除以整数。注解只在开发时提示，运行时并不检查类型
print("结论：类型注解是给人和 IDE 看的，运行时不做校验")

# 【动手改】给 calc_cpm 再加一个参数 unit: str = "元"，看注解里多出什么。


# ==== 9. 递归 ====
# 为什么：问题能拆成「同类型的更小问题」时（阶乘、树形结构），递归最自然。
# 是什么：函数自己调用自己，必须有终止条件，否则会 RecursionError。
def factorial(n: int) -> int:
    """n 的阶乘：n! = n * (n-1)!"""
    if n <= 1:              # 终止条件（基线条件）
        return 1
    return n * factorial(n - 1)   # 递归调用

print("5! =", factorial(5))                # -> 120
print("10! =", factorial(10))              # -> 3628800

# 递归做二分查找式的累加（演示拆问题思路）
def sum_to(n: int) -> int:
    return 0 if n == 0 else n + sum_to(n - 1)

print("1+...+100 =", sum_to(100))          # -> 5050

print("注意：Python 默认递归深度约 1000，太深要改用循环")

# 【动手改】把 factorial(5) 改成 factorial(0)，看终止条件是否生效。


# ==== 10. 函数作为参数（一等公民）====
# 为什么：把「怎么做」当参数传进去，同一个函数就能做不同的事。
# 是什么：函数可以赋值给变量、放进列表、作为参数传给别的函数。
def apply_metric(func, clicks, impressions):
    """用传入的指标函数计算一次"""
    return func(clicks, impressions)

print(apply_metric(calc_ctr, 360, 12000))          # -> 0.03
print(apply_metric(lambda c, i: c / i * 100, 360, 12000))   # -> 3.0

# 把函数存进字典，按名字调用
metrics = {
    "ctr": lambda c, i: c / i,
    "cpm": lambda c, i: c / i * 1000,
}
print("按名字调用:", metrics["ctr"](360, 12000))    # -> 0.03

# 内置的高阶函数：sorted / max / min 都接受 key
words = ["搜索", "信息流推广", "开屏"]
print("最长的渠道:", max(words, key=len))           # -> 信息流推广

# 【动手改】在 metrics 里加一个 "cpc": lambda cost, clicks: cost / clicks，调用试试。


# ===== 练习 =====
# 1. 写一个函数 calc_roi(revenue, cost)，返回投资回报率 (revenue - cost) / cost。
#    验证方式：calc_roi(1500, 1000) 得 0.5
# 2. 写一个函数，用 *args 求任意多个曝光量的总和。
#    验证方式：传入 12000、8000、5000 得 25000
# 3. 写一个函数返回列表的最小值、最大值、平均值，并解包接收。
#    验证方式：[1, 2, 3, 4] 得 1、4、2.5
# 4. 用 sorted + lambda 把 [("搜索", 12000), ("信息流", 8000)] 按曝光量降序排列。
#    验证方式：[('搜索', 12000), ('信息流', 8000)]

# ===== 参考答案 =====
print("\n--- 参考答案 ---")

# 1
def calc_roi(revenue, cost):
    return (revenue - cost) / cost

print("1.", calc_roi(1500, 1000))          # -> 0.5

# 2
def sum_impressions(*args):
    return sum(args)

print("2.", sum_impressions(12000, 8000, 5000))    # -> 25000

# 3
def stats(values):
    return min(values), max(values), sum(values) / len(values)

low, high, avg = stats([1, 2, 3, 4])
print(f"3. 最低 {low}，最高 {high}，平均 {avg}")     # -> 最低 1，最高 4，平均 2.5

# 4
channels = [("搜索", 12000), ("信息流", 8000)]
print("4.", sorted(channels, key=lambda x: -x[1]))
# -> [('搜索', 12000), ('信息流', 8000)]
