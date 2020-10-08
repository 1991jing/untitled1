import time




# #-*coding:utf-8-*
# import re
# def createid(matchobject,no=[0]):
#     no[0]+=1
#     return "[%d]"%no[0]
# text = "★A child is a human being who is not yet an adult.★A child is a human being who is not yet an adult.★A child is a human being who is not yet an adult."
# text=re.sub("★",createid,text)
# print(text)

import random

text=("test_goods_"+time.strftime('%Y-%m-%d-%H:%M:%S'))

print(text)
time.sleep(3)
print(text)

goods="test_goods_"+str(random.randrange(0,10000))
print(goods)




list=[1]