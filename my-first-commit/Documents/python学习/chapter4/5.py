 
name = "CherryGods"
a=b=c=''
index = 0
for i in name:
    if index == 0:
        a+=i
        if i == "e":
            index = 1
    elif index == 1:
        b+=i
        if i == "y":
            index = 2
    else: 
        c+=i
print(a)
print(b)
print(c)

