 
"""
要求:
1.将字符串的空白字符全部去掉
2.再使用" "作为分隔符，拼接成一个整齐的字符串
"""
poem_str = "春晓\n孟浩然\n春眠不觉晓 \t \t处处闻啼鸟\t \n夜来风雨声\t \t花落知多少"
print(poem_str)

# 1.分割字符串
poem_list = poem_str.split()
print(poem_list)
# 2.合并字符串
result = "|".join(poem_list)
print(result)
