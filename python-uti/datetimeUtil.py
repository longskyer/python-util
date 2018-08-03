#!/usr/bin/python
#coding=utf-8
import datetime

#获取今天的日期
def getToday():
    return datetime.datetime.today()
#获取年
def getYear():
    return getToday().year
#获取月
def getMonth():
    return getToday().month
#获取日
def getDay():
    return getToday().day
#获取小时
def getHour():
    return getToday().hour
#获取分钟
def getMinute():
    return getToday().minute
#获取秒数
def getSecond():
    return getToday().second
#根据date对象构造一个date
def getDate(aDate=datetime.date.today()):
    return datetime.date(aDate.year,aDate.month,aDate.day)
#获取date的年
def getYearOfDate(aDate=datetime.date):
    return aDate.year
#获取date的月
def getMonthOfDate(aDate=datetime.date):
    return aDate.month
#获取date的日
def getdayOfDate(aDate=datetime.date):
    return aDate.day
#获取时间
def getTime(aTime=datetime.time):
    return datetime.time(aTime.hour,aTime.minute,aTime.second,aTime.microsecond,aTime.tzinfo);

if __name__=="__main__":
    print getDate(datetime.date(2018,8,15))
    print getToday()
    print getYear(),getMonth(),getDay()
    print getHour()
    print getMinute()
    print getSecond()

