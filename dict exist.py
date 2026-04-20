def exist(dict3,key):
    if key in dict3:
        print("ELEMENT EXIST")
    else:
        print("ELEMENT NOT EXIST")
dict1={}
dict2={}
n=int(input("ENTER THE PAIRS OF DICT1: "))
m=int(input("ENTER THE PAIRS OF DICT2: "))
for i in range(n):
    key1=int(input("ENTER KEY1: "))
    val1=int(input("ENTER VALUE1: "))
    dict1[key1]=val1
dict3={}
for j in range(m):
    key2=int(input("ENTER KEY2: "))
    val2=int(input("ENTRE VALUE2: "))
    dict2[key2]=val2
print(dict1)
print(dict2)
dict3=dict(dict1.items() | dict2.items())
print(dict3)
key=int(input("ENTER KEY FOR CHECK: "))
exist(dict3,key)
