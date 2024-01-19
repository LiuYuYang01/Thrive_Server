from os import path, mkdir

# 生成文件唯一名称
def randomName(name):
    """当前时间戳 + 随机数 = 唯一值"""
    from time import time
    from random import randint

    # 文件后缀
    s = path.splitext(name)[1]

    # 获取当前时间戳
    t = int(time())

    # 生成一段随机数
    n = randint(0, 10000000)

    return f"{t}{n}{s}"
