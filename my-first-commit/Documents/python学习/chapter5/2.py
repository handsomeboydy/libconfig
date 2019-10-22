# 名片列表
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用［名片管理系统］V1.0", end="\n\n")
    print("1.新建名片\n2.显示全部\n3.查询名片\n\n0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("=" * 50)
    print("功能:新增名片")
    # 1.提示用户输入详细信息
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入QQ:")
    email = input("请输入邮箱:")
    # 2.根据信息追加名片字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    # 3.将名片字典添加到名片列表
    card_list.append(card_dict)
    # 4.提示用户添加成功
    print("添加%s成功!" % name)


def show_all():
    """显示全部"""
    print("功能:显示全部")
    # TODO 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有任何名片记录,请选择新增名片!")
        return
    # TODO 输出一个表头,进行排版
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")
    print("")
    print("=" * 50)
    # TODO 将列表的输出输出,并且格式化
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))


def find_card():
    """查询名片"""
    print("功能:查询名片")
    if len(card_list) == 0:
        print("当前没有任何名片记录,请选择新增名片!")
        return
    # TODO 1.提示用户要搜索的姓名
    find_name = input("请输入要搜索的姓名:")
    # TODO 2.遍历列表,查询要搜索的姓名,若不存在,则提示未查询到
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            # 3. TODO 针对搜索到的名片进行修改或删除操作的选择
            card_action(card_dict)
            break
    else:
        print("抱歉，没有找到%s" % find_name)
    print("=" * 50)


def card_action(card_dict):
    """
    修改功能
    :param card_dict:
    :return:
    """
    action = input("请输入对%s名片的操作:/1.修改/2.删除/0.返回上级菜单" % card_dict["name"])
    if action == "1":
        update = input("请要修改的类型:/1.姓名/2.电话/3.QQ/4.邮箱")
        if update in ["1", "2", "3", "4"]:
            if update == "1":
                card_dict["name"] = input("请输入要修改的姓名:")
            elif update == "2":
                card_dict["phone"] = input("请输入要修改的电话:")
            elif update == "3":
                card_dict["qq"] = input("请输入要修改的QQ:")
            elif update == "4":
                card_dict["email"] = input("请输入要修改的邮箱:")
            card_list.remove(card_dict)
            card_list.append(card_dict)
            print("修改成功！")
        else:
            print("输入有误！")
    elif action == "2":
        action = input("确定删除吗?(Y/N)")
        if action == "Y":
            card_list.remove(card_dict)
            print("删除成功！")
        elif action not in ["Y", "N"]:
            print("输入有误！")
show_menu()
#new_card()
#show_all()
#find_card()
card_action(card_dict)
