#coding=utf-8
dic = {'tom':11, 'sam':57,'lily':100}
print type(dic)

print dic['tom']
dic = {}
print dic
# 新增
dic['lilei'] = 99
# 循环使用
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print dic[key]
del dic['tom']
print dic.keys()           # 返回dic所有的键

print dic.values()         # 返回dic所有的值

print dic.items()          # 返回dic所有的元素（键值对）

dic.clear()                # 清空dic，dict变为{}

