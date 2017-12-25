#coding=utf-8
# 异常处理
re = iter(range(5))

# for i in range(100):
#     print re.next()
# 第6个会报错StopIteration 整个程序将会中断。

print 'hahaha'

try:
    t = 7
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end ',i, t

try:
    print(a*2)
except TypeError:
    print("TypeError")
except:
    print("Not Type Error & Error noted")

# try->异常->except->finally
# try->无异常->else->finally

print 'Lalala'
raise StopIteration  # 抛出异常
print 'Hahaha'

raise StopIteration()
