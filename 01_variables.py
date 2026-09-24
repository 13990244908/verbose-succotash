"""
《统计与数据分析》Python 基础 01：变量

学习目标：
  1. 理解 `=` 是把名字绑定到对象，而不是把值装进盒子里。
  2. 知道变量本身没有类型，对象才有类型（动态类型）。
  3. 掌握合法标识符、命名惯例，以及常见内置类型长什么样。
  4. 会用多重赋值、解包、类型转换和 f-string 输出广告投放指标。

运行方法：
  在 VSCode 里打开本文件，点右上角 ▶ Run Python File，或按 Ctrl + F5；
  或在命令行执行：python 01_variables.py

提示：文件末尾有练习与参考答案。想先自己做，就把「参考答案」那一段注释掉再运行。
"""

import keyword  # 标准库，用来查看 Python 的关键字列表

# ==== 1. 变量是什么 ====
# 为什么：同一份数据要反复使用，给它起个名字就不用重复写。
# 是什么：`=` 不复制值，只是让左边的名字指向右边那个对象。
campaign = "夏季促销"
alias = campaign
print("campaign =", campaign)                                  # -> campaign = 夏季促销
print("id(campaign) == id(alias):", id(campaign) == id(alias))  # -> True

# 重新赋值只是让名字换个指向，原来的对象不受影响
alias = "618 大促"
print("campaign =", campaign)                                   # -> campaign = 夏季促销
print("alias =", alias)                                         # -> alias = 618 大促

# 【动手改】把 alias = "618 大促" 改成 alias = campaign，重新运行看是否仍指向同一对象。


# ==== 2. 动态类型 ====
# 为什么：同一个名字后面可以换成别的东西，这是 Python 灵活的地方。
# 是什么：变量没有类型，类型跟着对象走；type() 看的是当前指向的那个对象。
metric = 0.032                  # 点击率
print(type(metric))             # -> <class 'float'>
metric = "click_rate"           # 换成指标名
print(type(metric))             # -> <class 'str'>
metric = [0.032, 0.028, 0.041]  # 换成一组点击率
print(type(metric))             # -> <class 'list'>

# 【动手改】把最后一行改成 metric = {"ctr": 0.032}，看类型变成什么。


# ==== 3. 命名规则与惯例 ====
# 为什么：名字写错会直接语法错误；团队里还要有统一的命名习惯。
# 是什么：标识符由字母、数字、下划线组成，不能以数字开头，区分大小写，且不能是关键字。
valid_name = 1          # 合法：字母 + 下划线
_name2 = 2              # 合法：下划线开头
ClickRate = 3           # 合法但不符合惯例，PEP 8 建议全小写
# 2clicks = 4           # SyntaxError：不能以数字开头
# click-rate = 4        # SyntaxError：中划线会被当成减号
# class = 4             # SyntaxError：class 是关键字

print("关键字个数:", len(keyword.kwlist))             # -> 关键字个数: 35
print("'class' 是关键字吗:", keyword.iskeyword("class"))   # -> True

clicks = 1000
CLICKS = 2000           # 大小写不同，就是两个不同的名字
print(clicks, CLICKS)   # -> 1000 2000

MAX_CLICKS = 5000       # 惯例：常量全大写 + 下划线
click_rate = 0.032      # 惯例：普通变量用 snake_case
print("MAX_CLICKS =", MAX_CLICKS)                     # -> MAX_CLICKS = 5000

# 【动手改】把 valid_name 改成 validName，重新运行（不报错，但不符合 PEP 8）。


# ==== 4. 内置类型一览 ====
# 为什么：数据长什么样，决定了你能对它做什么运算。
# 是什么：下面每一行都是一个对象，type() 直接告诉你它的类型。
impressions = 12000                     # int：整数，曝光量
ctr = 0.032                             # float：小数，点击率
campaign_name = "夏季促销"               # str：字符串
is_active = True                        # bool：布尔值，投放中？
remark = None                           # NoneType：空值，尚未填写
channels = ["搜索", "信息流", "开屏"]     # list：列表，有序可变
coords = (116.4, 39.9)                  # tuple：元组，有序不可变
tags = {"新客", "高价值", "新客"}         # set：集合，无序去重
kpi = {"ctr": 0.032, "cvr": 0.015}      # dict：字典，键值对

for value in [impressions, ctr, campaign_name, is_active, remark,
              channels, coords, tags, kpi]:
    # 集合无序，直接打印顺序不固定；排序后再输出，保证每次运行结果一致
    shown = sorted(value) if isinstance(value, set) else value
    print(f"{str(shown):<26} -> {type(value).__name__}")

print("tags（重复的'新客'被去掉）:", sorted(tags))   # -> ['新客', '高价值']
print("{} 的类型:", type({}).__name__)             # -> dict
print("空集合要写 set():", type(set()).__name__)   # -> set

# 【动手改】往 tags 里再加一个已存在的值，看输出是否变化。


# ==== 5. 多重赋值与解包 ====
# 为什么：一次给多个名字赋值、或把一组数据拆开，代码更短更清楚。
# 是什么：右边先整体求值，再按位置一一对应地赋给左边。
impressions, clicks, cost = 12000, 360, 890.5
print(impressions, clicks, cost)          # -> 12000 360 890.5

# 交换两个变量，不需要临时变量
a, b = 10, 20
a, b = b, a
print("交换后:", a, b)                     # -> 交换后: 20 10

# 星号解包：把剩下的都收进一个列表
top, *rest = [0.041, 0.032, 0.028, 0.025]
print("top =", top)                       # -> top = 0.041
print("rest =", rest)                     # -> rest = [0.032, 0.028, 0.025]

# 【动手改】把 12000, 360, 890.5 改成 4 个值再运行（会报错：数量要对应）。


# ==== 6. 可变与不可变 ====
# 为什么：同样的「改一下」，有的类型真的改了，有的直接报错——这是最常见的坑。
# 是什么：list/dict/set 可变（能原地改）；int/float/str/tuple 不可变（只能重新赋值）。
channels = ["搜索", "信息流"]
channels.append("开屏")                   # 原地修改
print(channels)                           # -> ['搜索', '信息流', '开屏']

name = "夏季促销"
# name[0] = "冬"                          # TypeError：str 不可变
name = "冬季促销"                          # 只能让名字指向新字符串
print(name)                               # -> 冬季促销

# 传参时的差别：函数里改 list 会影响外面（04、05 号文件细讲）
def add_channel(lst):
    lst.append("激励视频")

channels_copy = ["搜索"]
add_channel(channels_copy)
print("函数外也变了:", channels_copy)       # -> ['搜索', '激励视频']

# 【动手改】把 channels.append("开屏") 换成 channels = channels + ["开屏"]，体会两者区别。


# ==== 7. 类型转换 ====
# 为什么：从文件、表单读到的数据常常是字符串，要转成数字才能计算。
# 是什么：int() / float() / str() / bool() 把一个类型转成另一个类型。
ctr_text = "0.032"
print(type(ctr_text))                     # -> <class 'str'>
ctr_num = float(ctr_text)
print(ctr_num, type(ctr_num))             # -> 0.032 <class 'float'>

print(int(3.9))                           # -> 3（直接截断，不是四舍五入）
print(round(3.9))                         # -> 4
print(bool(0), bool(1), bool(""), bool("0"))   # -> False True False True
print("记住：0、空字符串、None 都是假；非零数字、非空字符串都是真")

# 字符串不能直接和数字相加
# print("点击率" + 0.032)                 # TypeError
print("点击率" + str(0.032))               # -> 点击率0.032

# 【动手改】把 int(3.9) 改成 int(-3.9)，看是 -3 还是 -4（向 0 截断）。


# ==== 8. f-string 格式化输出 ====
# 为什么：报表要控制小数位、加百分号、对齐列，直接 print 变量不够用。
# 是什么：字符串前加 f，花括号里写变量或表达式，冒号后写格式说明。
impressions, clicks = 12000, 360
ctr = clicks / impressions
gmv = 45890.5678

print(f"曝光 {impressions}，点击 {clicks}，点击率 {ctr:.2%}")   # -> 点击率 3.00%
print(f"成交额 ¥{gmv:,.2f}")                                  # -> ¥45,890.57
print(f"{'渠道':<8}{'曝光':>10}")                              # 左对齐 / 右对齐
print(f"{'搜索':<8}{impressions:>10}")
print(f"CTR 的 2 倍是 {ctr * 2:.4f}")                          # 花括号里能写表达式

# 【动手改】把 {ctr:.2%} 改成 {ctr:.4%}，看小数位怎么变。


# ===== 练习 =====
# 1. 定义 impressions = 15000、clicks = 480，计算并输出点击率（两位小数百分比形式）。
#    验证方式：应输出 3.20%
# 2. 把字符串 "15000" 转成整数，加上 2000，再转回字符串。
#    验证方式：最终类型是 str，值是 "17000"
# 3. 用一行多重赋值给 a、b、c 分别赋 1、2、3，然后交换 a 和 b 的值。
#    验证方式：交换后 a=2、b=1、c=3
# 4. 判断下面哪些是可变类型：list、str、tuple、dict、set、int。
#    验证方式：可变的是 list、dict、set

# ===== 参考答案 =====
print("\n--- 参考答案 ---")

# 1
impressions, clicks = 15000, 480
print(f"1. 点击率 {clicks / impressions:.2%}")        # -> 3.20%

# 2
value = str(int("15000") + 2000)
print(f"2. {value}，类型 {type(value).__name__}")      # -> 17000，str

# 3
a, b, c = 1, 2, 3
a, b = b, a
print(f"3. a={a}, b={b}, c={c}")                      # -> a=2, b=1, c=3

# 4
mutable = [t for t in ["list", "str", "tuple", "dict", "set", "int"]
           if t in ("list", "dict", "set")]
print("4. 可变类型:", mutable)                          # -> ['list', 'dict', 'set']
