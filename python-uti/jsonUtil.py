#!/usr/bin/python
#coding=utf-8
import json
#json字符串转换成python对象
def json2Object(str):
    return json.loads(str)
#python对象转换成json字符串
def object2Json(dict):
    return json.dumps(dict);
#从test.txt文件读取json字符串后转换成python对象
def fileJson2Object(aFile=open("test.txt","rw")):
    return json.load(aFile)
#将python对象序列化成json后写入文件test.txt
def object2FileJson(dict={},aFile=open("test.txt","rw")):
    return json.dump(dict,aFile)
