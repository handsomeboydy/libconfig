# 全局变量
name = "王五"


def demo1():
    # 希望修改全局变量
    # 在Python中函数中是不能直接修改全局变量的
    # 所以这里只是创建了一个局部变量
    name = "飞机"
    print("你好，%s" % name)


def demo2():
    print("你好，%s" % name)


demo1()
demo2()
