"""
定义一个布尔型变量has_ticket表示是否有车票
定义一个整型变量knife_length表示刀的长度，单位:厘米
首先检查是否有车票，如果有允许进行安检
安检时，需要检查刀的长度，判断是否超过20厘米，
    如果超过20厘米，提示刀的长度，不允许上车
    如果不超过20厘米，安检通过
如果没有车票不允许进门
"""
has_ticket = True
knife_length = 21
if has_ticket:
    print("车票检查通过，开始安检")
    if knife_length > 20:
        print("刀的长度:%d" % knife_length+"，不允许上车")
    else:
        print("安检通过可以上车")
else:
    print("没有车票，不允许上车")
