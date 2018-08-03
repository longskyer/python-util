#!/usr/bin/python
#coding=utf-8

import random
import string

#获取指定范围的随机整数
def getRandomInt(a,b):
    return random.randint(a,b)
#获取指定范围的随机偶数
def getRandomEven(a,b):
    return random.randrange(a, b, 2)
#获取指定范围的随机浮点数
def getRandomFloat(a,b):
    return random.uniform(a,b)

#获取0-1之间的随机浮点数
def getRandomLessThanOne():
    return random.random()
#获取随机小写字母
def getRandomLowerLetter():
    return random.choice(string.ascii_lowercase)
#获取随机数字
def getRandomDigit():
    return random.choice(string.digits)
#获取随机字母，不分大小写
def getRandomLetter():
    return random.choice(string.ascii_letters)
#洗牌
def shuffle(aList):
    return random.shuffle(aList)
#随机返回列表中的一个元素
def getRandomOne(aList):
    return random.choice(aList)
#随机返回列表中的n个元素
def getRandomMuti(aList,n):
    return random.sample(aList,n)

if __name__=="__main__":
    print getRandomEven(0,100)
    print getRandomInt(5,9)
    print getRandomLowerLetter()
    print getRandomFloat(0,1000)
    print getRandomMuti(["qeqee","hhjj","gfgg","rju"],2)
    print getRandomOne(["rrtt","tttt","ghgygy"])
    print getRandomLetter()
    print getRandomDigit()
