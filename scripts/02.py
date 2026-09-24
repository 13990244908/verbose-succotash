# 这是Python中的注释

"""
这也是Python中的注释，用三个引号（可以是单引号或双引号）括起来的多行字符串。
它通常用于文档字符串（docstring）或多行注释。
"""


def greet(name):
    """问候某人（这是一个 docstring 示例）。

    参数:
        name (str): 对方的名字

    返回:
        str: 问候语
    """
    return f"你好，{name}！"


if __name__ == "__main__":
    print(greet("同学"))
