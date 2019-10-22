import random

# 从控制台输入要输出的类型(剪刀１石头２布３)
player = int(input("请出拳(剪刀１石头２布３):"))
pc = random.randint(1, 3)
print("玩家出的:%d\n电脑出的:%d" %(player,pc))
if ((player == 1 and pc == 3)
        or (player == 2 and pc == 1)
        or (player == 3 and pc == 2)):

    print("玩家胜!")
elif player == pc:
    print("平局")
else:
    print("电脑胜")
