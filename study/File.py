#coding=utf-8

f = open("test.txt","r")
content = f.read(5)          # 读取N bytes的数据
print  content
content = f.readline()       # 读取一行
print content

f = open("test.txt","w")
f.write('I like apple')      # 将'I like apple'写入文件
f.close()