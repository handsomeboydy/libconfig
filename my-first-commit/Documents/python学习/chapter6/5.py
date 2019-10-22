# 全局变量应该定义在所有函数的上方
name = "张三"


def test01():
    print(name)
    print(my_name)
    # print(you_name)


my_name = "CherryGods"
test01()
# 这里是报错的
# you_name = "李四"
