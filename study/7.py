#!/usr/bin/env python
# coding=utf-8

n1 = [1,2,3,4,5]

print n1.count(5) #计数，看总共多少个5
print n1.index(3) #查询n1第一个3的下标
n1.append(6) #n1最后添加元素6
n1.sort() #对n1进行排序
print n1.pop() #从n1去除最后一个元素
n1.remove(2) #从n1去除第一个2
n1.insert(0,9) #在下标为0的位置插入9

print [1,2,3] + [5,6,7]
