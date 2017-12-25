# coding=utf-8

# 关键字(keyword)传递是根据每个参数的名字传递参数。
def f(a,b,c):
    print c,b,a
    return a+b+c
print(f(c=3,b=2,a=1))

#参数默认值
def f(a,b,c=10):
    return a+b+c
print(f(3,2))
#包裹传递
#在定义函数时，我们有时候并不知道调用的时候会传递多少个参数
def func(*name):
    print type(name)
    print name
func(1,4,6)
func(5,6,7,1,2,3)
#在func的参数表中，所有的参数被name收集，根据位置合并成一个元组(tuple)
def func(**dict):
    print type(dict)
    print dict
func(a=1,b=9)
func(m=2,n=1,c=11)
#dict是一个字典，收集所有的关键字，传递给函数func。为了提醒Python，参数dict是包裹关键字传递所用的字典，在dict前加**。
#包裹传递的关键在于定义函数时，在相应元组或字典前加*或**。

#解包裹
#*和**，也可以在调用的时候使用，即解包裹(unpacking)
def func(a,b,c):
    print a,b,c
args = (1,3,4)
func(*args)
#就是在传递tuple时，让tuple的每一个元素对应一个位置参数

dict = {'a':1,'b':2,'c':3}
func(**dict)
#在传递词典dict时，让词典的每个键值对作为一个关键字传递给func。

#混合
#先位置，再关键字，再包裹位置，再包裹关键字

