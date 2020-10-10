
# def jiafa(x,y):
#     return x+y
#
# print(jiafa(5,4))
# print("end")

# import json
# s= "A:1|B:2|C:3|D:4".split('|')
# print(s)
# d= dict()
# print(d)
# for temp in s:
#     # print(temp[0]), print(temp[1]), print(temp[2])
#    d[temp[0]] = temp[2]
# print(str(d))
#
# t=json.loads(str(d).replace('\'', "\""))
# print(t)


# def test():
#     print('1')
#
# print(test())
# print('2')
#
#
# class num():
#     y=2
#
# a=num.y
# print(a)


import sys
import os


print (os.getcwd()) # 当前工作路径
print (sys.argv) # 输入参数列表
print (sys.argv[0]) # 第0个就是这个python文件本身的路径（全路径）

# Python文件名 相当于是上面保留的最后一部分 即*.py
print (sys.argv[0][sys.argv[0].rfind(os.sep) + 1:] )


from pathlib import Path
name=Path(__file__).name.split(".py")[0]

print(name)