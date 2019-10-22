import cards_tools
while True:
    cards_tools.show_menu()
    action = str(input("请选择操作系统:"))
    print("您选择的操作系统是[%s]" % action)
    # TODO 针对名片的操作
    if action in ["1", "2", "3"]:
        # 如果不想在分支内部立刻编写代码,可以使用pass表示一个占位符使得程序变得正确
        # TODO 新增名片
        if action == "1":
            cards_tools.new_card()
            pass
        # TODO 显示全部
        elif action == "2":
            cards_tools.show_all()
            pass
        # TODO 查询名片
        elif action == "3":
            cards_tools.find_card()
            pass
    # TODO 输入0时退出
    elif action == "0":
        print("已退出.")
        break
    else:
        print("输入错误,请重新输入!")
