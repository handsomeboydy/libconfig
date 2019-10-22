test_str = "TestTestTestT"
# 统计字符串的长度
print(len(test_str))
# 统计某个子字符串在字符串存在了多少次
# 如果count方法內的参数在字符串中不存在，那么则返回0
print(test_str.count("T"))
# 某个子字符串出现的位置
# 如果参数內的值在字符串中不存在那么就会报错
print(test_str.index("stT"))
