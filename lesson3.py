# -*- coding: utf-8 -*-


'''
练习1.2.1-顺序逻辑:
1)早上吃大饼加鸡蛋火腿
2)上班操盘盈利股票交易，当日盈利today_profit
3)晚上吃麦当劳
'''

# import random
# print('吃大饼加火腿鸡蛋')
# profit =  round(random.random(),2)
# print('当日盈利:',profit,'元')
# print('吃大饼加火腿鸡蛋')


'''
练习1.2.2- if:
1)早上吃大饼加鸡蛋火腿
2)上班操盘盈利股票交易，当日盈利today_profit元
3)如果当日盈利大于9万，晚上吃海鲜
   如果当日盈利不到9万，大于5万，吃麦当劳
   如果当日盈利不到5万， 吃煎饼果子
   如果当日不盈利， 饿肚子

扩展:当日不盈利，但是有人请吃饭，蹭饭吃
'''
# import random
# print('吃大饼加火腿鸡蛋')
# profit =  round(random.random()*100000/10000,2)
# print('当日盈利:', profit, '万元')
# if profit > 9:
#     print('吃海鲜')
# elif profit >5:
#     print('麦当劳')
# else :
#     print('煎饼果子')
#
# print('吃大饼加火腿鸡蛋')

'''
练习1.2.3-使用for循环:
1)30天工作安排
连续工作5天，上班搬砖
休息2天，去水上公园玩
'''
# for i in range(30):
#     print('第',i,'天：')
#     if i%7 <5:
#         print('上班搬砖')
#     else:
#         print('去水上公园玩')

'''
2)2020年5月份
如果当日开盘，上班搬砖
如果当日不开盘，去水上乐园玩

扩展:彩票中奖500(采用随机数大于0.9999实现)，辞职不上班
'''
# import datetime as dt
# import random
# current_date = dt.datetime.strptime('2020-05-01','%Y-%m-%d')
# current_date = current_date.date()
#
# while current_date.month <= 5:
#     print(current_date)
#     if current_date.weekday() <5:
#         print('上班搬砖')
#     else:
#         print('去水上乐园耍')
#     current_date += dt.timedelta(days=1)
#
#     result = random.randint(1,10000)
#     if result > 9999:
#         print('辞职不上班')
#         break


'''
练习1.2.4-使用while循环:
每天买固定号码双色球
7,9,16,22,24,32,06
如果当日中头等奖，辞职去旅行
否则继续搬砖

并打印买了多少天彩票才中奖，
扩展:
如果前6个数字，中了3个数字吃煎饼果子，如果中了4个数字吃麦当劳，如果中了5个数字，吃海鲜
如果最后一个数字中了，加个鸡蛋
'''
# import random
# def win_lottery_twoball():
#     data_buy=[7,9,16,22,24,32,6]
#     data_lottery = []
#     #模拟彩票抽奖
#     for i in range (7):
#         data_lottery.append(random.randint(1,33))
#     #验证
#     for i in range (3):
#         # print('databuy:',dataBuy[i])
#         # print('dataLottery:',dataLottery[i])
#         if(data_buy[i] != data_lottery[i]):
#             return  False
#     return  True
#
#
# #
# import random
# def win_lottery_twoball_count():
#     data_buy=[7,9,16,22,24,32,6]
#     data_lottery = []
#     #模拟彩票抽奖
#     for i in range (7):
#         data_lottery.append(random.randint(1,33))
#     #验证
#     win_count = 0
#     for i in range (7):
#         if(data_buy[i] == data_lottery[i]):
#             win_count +=1
#     return  win_count
#
# # #模拟买彩票buyCount次
# # buyCount = 100000000
# # for i in range (buyCount):
# #     if winLotteryTwoBall():
# #         print('第{}次购买，中奖啦！！！！！！！！！！！！！！！'.format(i+1))
# #         break
# #     if i + 1 %1000000 ==0 :
# #         print(('第{}次购买，未中奖').format(i+1))
#
# #模拟买彩票 直到买中
# buyCount = 0
# while True:
#     buyCount +=1
#     # if winLotteryTwoBall():
#     #     print('第{}次购买，中奖啦，辞职去旅行！！！！！！！！！！！！！！！'.format(buyCount))
#     #     break
#     # print('继续当交易员，搬砖')
#     #
#     win_count = win_lottery_twoball_count()
#     if(win_count ==7):
#         print('第{}次购买，中奖啦，辞职去旅行！！！！！！！！！！！！！！！'.format(buyCount))
#     elif (win_count ==6):
#         print('吃海鲜')
#     elif (win_count ==5):
#         print('吃麦当劳')
#     elif (win_count ==4):
#         print('吃煎饼果子')
#
#     if buyCount %1000000 ==0 :
#         print(('第{}次购买，未中奖').format(i+1))


'''
练习1.2.5-综合练习
收盘价大于最近50天均价，买入
收盘价小于最近50天均价，卖出
'''
close_price_list=[12.72,12.31,12.25,12.43,12.27,12.16,12.22,12.24,12.36,12.27,12.09,12.05,11.78,11.73,11.85,11.8,12.21,12.52,12.44,12.46,12.36,12.54,12.67,12.93,13.66,13.5,13.55,13.29,13.37,13.71,13.78,13.93,14.18,14.01,13.99,13.92,13.59,13.59,13.56,13.54,14.12,14,13.75,13.69,13.67,13.99,13.85,13.76,13.88,14.2,14.23,14.29,14.37,14.13,14.1,13.74,13.35,13.37,13.54,14.38,14.52,15.12,14.89,14.97,14.94,14.9,14.92,14.99,14.45,14.31,14.65,14.25,14.31,14.27,14.13,14.16,14.45,14.3,14.44,14.58,14.81,14.69,14.55,14.56,14.68,14.45,14.24,14.41,14.84,15.34,15.38,15.18,15.75,15.71,15.9,15.59,16.2,16.25,16.24,16.81,17.22,17.18,16.79,16.7,16.51,16.89,16.42,16.45,16.87,16.88,16.66,16.91,16.43,16.26,16.86,16.92,17.15,16.96,16.89,16.65,16.28,16.33,16.33,16.32,16.34,16.45,16.41,15.85,15.86,15.59,15.8,15.62,15.47,15.49,15.29,15.36,15.45,15.31,15.43,15.6,15.41,15.33,15.66,15.6,16.12,16.13,16.5,16.46,16.55,16.59,16.24,16.4,16.3,16.47,16.63,16.57,16.45,16.87,17.18,17.07,17.15,16.66,16.79,16.69,16.99,16.76,16.52,16.33,16.39,16.45,16,16.09,15.54,13.99,14.6,14.63,14.77,14.62,14.5,14.79,14.77,14.65,15.03,15.37,15.2,15.24,15.59,15.58,15.23,15.04,14.99,15.11,14.5,14.79,14.72,14.69,15.39,15.03,14.45,14.76,14.69,14.68,14.52,13.75,13.41,12.71,12.23,12.52,12.15,12.61,12.87,13.06,13.15,12.94,12.8,12.89,12.97,12.61,12.88,12.78,12.74,12.79,12.59,12.86,12.87,12.68,12.89,12.99,13.45,13.23,13.23,13.24,13.5,13.52,14.02,13.93,13.77,13.69,13.95,14,13.79,13.63,13.3,13.23]
ma5_array = []
ma10_array = []
for i in range(len(close_price_list)):
    #计算5日均线
    ma5=0
    ma5_sum_count = 0
    for j in range(5):
        if(i-j >=0):
            ma5 += close_price_list[i-j]
            ma5_sum_count +=1
    ma5 /=ma5_sum_count
    ma5_array.append(ma5)
    #计算10日均线
    ma10=0
    ma10_sum_count = 0
    for j in range(10):
        if(i-j >=0):
            ma10 += close_price_list[i-j]
            ma10_sum_count +=1
    ma10 /=ma10_sum_count
    ma10_array.append(ma10)
    #print('收盘价:{},MA5:{},MA10:{}'.format(close_price_list[i],round(ma5,2),round(ma10,2)))
    if i>0:
        if ma5 > ma10 and ma5_array[i-1] < ma10_array[i-1] :
            print("买入持有:价格",close_price_list[i])
        elif ma5 < ma10 and ma5_array[i-1] > ma10_array[i-1]:
            print("卖出持仓:价格",close_price_list[i])
        else:
            pass





