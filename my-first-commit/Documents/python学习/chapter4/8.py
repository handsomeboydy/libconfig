test_str = "Hello World"
# 1.判断是否以某个字符串开头
print(test_str.startswith("Hello"))
# 2.判断是否以某个字符串结尾
print(test_str.endswith("World"))
# 3.查找指定的字符串的索引位置
print(test_str.find("o"))
# 如果没有找到则返回-1
print(test_str.find("不存在"))
# 4.替换字符串，会将返回一个新字符串，里面存着替换后的字符串
# 并且不会替换原有的字符串
print(test_str.replace("World", "Python"))
print(test_str)
