#!/usr/bin/env python
# coding=utf-8
# 对象的性质

class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print self.gender
li_lei = Human('male') #这里，`male`作为参数还给__init__()方法的input_gender变量
print li_lei.gender
li_lei.printGender()
