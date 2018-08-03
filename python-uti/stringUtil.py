#!/usr/bin/python
#coding=utf-8
import string

#把字符串转换成小写字母
def toLower(str=''):
    return str.lower()
#首字母大写
def capitalize(str=''):
    return str.capitalize()
#字符串转换成大写字母
def toUpper(str):
    return str.upper()
#以指定编码编码字符串
def encode(str='',encoding='utf-8',errors='strict'):
    return str.encode(encoding,errors)
#以指定编码解码字符串
def encode(str='',encoding='utf-8',errors='strict'):
    return str.encode(encoding,errors)
#是否都是数字
def isDigit(str=''):
    return str.isdigit()
#判断是否都是字母
def isAlpha(str=''):
    return str.isalpha()
#判断是否都是小写
def isLower(str=''):
    return str.islower();
#判断是否都是数字或者字母
def isAlnum(str=''):
    return  str.isalnum();
#判断是否都是大写
def isUpper(str=''):
    return str.isupper()
#去掉左边不可见字符
def lStrip(str=''):
    return str.lstrip();
#去掉右边不可见字符
def rStrip(str=''):
    return str.rstrip();
#去掉两端不可见字符
def strip(str=''):
    return str.strip()
#根据分隔符返回列表
def split(str='',sep=' '):
    return str.split(sep)
#大小写互换
def swapCase(str=''):
    return string.swapcase(str)
if __name__=="__main__":
    print toLower("QWERTYYUYUUU")
    print capitalize("longskyer")
    print toUpper("asdffgg")
    print isLower()
    print lStrip('            asdfgfg')
    print split("ddd ghhh")
