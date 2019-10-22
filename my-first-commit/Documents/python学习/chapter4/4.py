'''
 使用　多个键值对，存储描述一个物体的信息
 一个列表中存储多个键值对，并且对其遍历
'''
student01 = {"name": "CherryGods",
             "age": 16
             }
student02 = {"name": "Test",
             "age": 17
             }
test_list = [student01, student02]

for i in test_list:
    for j in i:
        print("%s - %s" % (j, i[j]))
