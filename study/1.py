#!/usr/bin/env python
# coding=utf-8
#面向对象
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
summer = Bird()
print 'after move:',summer.move(5,8)
