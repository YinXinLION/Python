#coding=utf-8
#在Python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列的下标。

#range()
S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]

#enumerate()
#可以在每次循环中同时得到下标和元素
S = 'abcdefghijk'
for (index,char) in enumerate(S):
    print index
    print char
#enumerate()在每次循环中，返回的是一个包含两个元素的定值表(tuple)

#zip()
#zip()函数起到了聚合列表的功能。
#如果你多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素，
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)
#每次循环时，从各个序列分别从左到右取出一个元素，合并成一个tuple，然后tuple的元素赋予给a,b,c
ta = [1,2,3]
tb = [9,8,7]

# cluster
zipped = zip(ta,tb)
print(zipped)

# decompose
na, nb = zip(*zipped)
print(na, nb)

#循环对象
#循环对象是这样一个对象，它包含有一个next()方法。__next__()方法，在python 3x中
#这个方法的目的是进行到下一个结果，而在结束一系列结果之后，举出StopIteration错误。

#open()返回的实际上是一个循环对象,包含有next()方法
#而该next()方法每次返回的就是新的一行的内容，到达文件结尾时举出StopIteration。
for line in open('test.txt'):
    print line

#迭代器
#技术上来说，循环对象和for循环调用之间还有一个中间层，就是要将循环对象转换成迭代器(iterator)。
# 这一转换是通过使用iter()函数实现的。
# 但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方。

#生成器
#主要目的是构成一个用户自定义的循环对象。
#生成器的编写方法和函数定义类似，只是在return的地方改为yield。
#生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。
#当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield
#生成器自身又构成一个循环器，每次循环使用一个yield返回的值。
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000
for i in gen():
    print i

def gen():
    for i in range(4):
        yield i
print "-----"
G = (x for x in range(4))  #生成器表达式
print G
#表推导是快速生成表
L = []
for x in range(10):
    L.append(x**2)
#表推导的方式 L = [x**2 for x in range(10)]
print "---"
print L
print "---"
x1 = [1,3,5]
y1 = [9,12,13]
L = [ x**2 for (x,y) in zip(x1,y1) if y > 10]  #[9,25]
print L
