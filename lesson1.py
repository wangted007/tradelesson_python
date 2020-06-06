# -*- coding: utf-8 -*-


# #所有关键词
#import keyword
# print(keyword.kwlist)
# #迭代
# keyword_count = len(keyword.kwlist)
# print('keyword count:',keyword_count)
# for i in range (keyword_count):
#     print(keyword.kwlist[i])


#命名规则
# 使用范围  大小写字母，数字，下划线
#不能使用关键字
#数字不能在前

# #错误案例
# break = 10
# zhang-san  = 'zhang san'
# ___personName = 'lisi'
# David.Wang = 'David . Wang'
# 2_student_count = 100


# #数据类型
# print(type(1))
# print(type(False))
# print(type(10.56))
# print(type('aaaaa'))

# #以下是什么类型
# price = '10.56'
# print(type(price))

# #问题  以下输出什么结果？
# print(type(print))
# print(type(keyword))

# pre_close=10.34
# close_price = 10.56
# print(close_price)
# volume = 1063500
# amount = 11015630.50
# average_price = amount/volume
# print(average_price)
# code='000001.sz'
# trade_date='2020-05-06'
# is_index = False
# print("stock info,code:{},trade date:{},close price:{},amount:{}，average price:{}".format(code,trade_date,close_price,amount,average_price))

# #类型转换
# price = 10.56
# print(type(price))
# price = 10
# print(type(price))
# price = int(price)
# print(type(price))

# #运算符
# #算术运算符 + - * / % ** //
# print( 103 / 10 )
# print( 103 % 10 )
# print( 103 // 10 )
# print(2**10)

# #逻辑运算符
# # == != > < >= <=
# #返回结果是个bool值
# print(1 == 0.999)
# print(1 == 0.99999999999999999)
# print(10.02999999999999)

# #字符串比较
# stock1 = '000001.sz'
# stock2 = '600000.sh'
# stock3 = '000001.sz'
# print(stock1 == stock2)
# print(stock1 == stock3)


# #赋值运算符 =
# pre_close_price = 10.35
# close_price = 10.40
# updown_value = close_price - pre_close_price
# updown_rate = updown_value/close_price *100
# print(updown_value,updown_rate)
# updown_value = round(updown_value,2)
# print(updown_value)

# import random
# prices = []
# for i in range (10):
#     prices.append(round(10+ random.random(),2))
# print(prices)
#
# sum = 0
# for i in range (len(prices)):
#     sum = sum + prices[i]
#     #sum += prices[i]
# print(sum)


# #常量和变量
#from math import *
# print(pi)
#
# radius = 40
# area = pi* radius**2
# print(round(area))
#
# print(e)
# print(inf)
# print(nan)


# 会使用help
#import math
#help(math.pi)
#help(type)
#help(math)