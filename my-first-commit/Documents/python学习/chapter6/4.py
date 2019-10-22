# 全局变量
name = "菠萝"


def test01():
    # 声明这个name就是全局变量
    global name    #同时修改全局变量
    name = "飞机"
    print(name)


def test02():
    # 这里没有声明global所以是用的局部变量
    name = "香蕉皮"
    print(name)

def test03():
    print(name)
test01()
test02()
test03()
