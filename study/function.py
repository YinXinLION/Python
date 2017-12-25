#coding=utf-8
#函数对象

#lambda函数
func = lambda x,y: x + y
print func(3,4)

# 函数作为参数传递
# 函数可以作为一个对象，进行参数传递。
def test(f, a, b):
    print 'test'
    print f(a, b)

test(func, 3, 5)

test((lambda x,y: x**2 + y), 6, 9)

# map函数 内置函数
re = map((lambda x: x+3),[1,3,5,6])
print re
#map()的功能是将函数对象依次作用于表的每一个元素,每次作用的结果储存于返回的表re中
#在Python 3.X中，map()的返回值是一个循环对象。可以利用list()函数，将该循环对象转换成表。
#map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数。
re = map((lambda x,y: x+y),[1,2,3],[6,7,9])

# filter()函数
# filter函数的第一个参数也是一个函数对象。它也是将作为参数的函数对象作用于多个元素。
# 如果函数对象返回的是True，则该次的元素被储存于返回的表中。
# filter通过读入的函数来筛选数据。 在Python 3.X中，filter返回的不是表，而是循环对象。
def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])

# reduce()函数
# reduce可以累进地将函数作用于各个参数
print reduce((lambda x,y: x+y),[1,2,5,7,9])   # (((1+2)+5)+7)+9
# reduce的第一个参数是lambda函数，它接收两个参数x,y, 返回x+y。

# reduce将表中的前两个元素(1和2)传递给lambda函数，得到3。
# 该返回值(3)将作为lambda函数的第一个参数，而表中的下一个元素(5)作为lambda函数的第二个参数，进行下一次的对lambda函数的调用，得到8。
# 依次调用lambda函数，每次lambda函数的第一个参数是上一次运算结果，而第二个参数为表中的下一个元素，直到表中没有剩余元素。