import sys

#演示函数
def test_func():
    print(__name__)
    print(sys._getframe().f_code.co_name)

#演示参数
def test_func_para(name ,age,score,city="天津"):
    print("{}来自{},的年龄为{}，数学考试得分{}".format(name,city,age,score[1]))

    student = {}
    student['name'] = name
    student['age'] = age
    student['score'] = score
    student['city'] = city
    return student

city_list = {
    'BJ':{
        "code":"BJ",
        "name":"北京",
        "phone": "010",
    },
    'TJ': {
        "code": "TJ",
        "name": "天津",
        "phone": "022",
    }
}
#演示返回值
def test_func_return(name ,citycode="TJ"):
    city = city_list[citycode]
    print("{}来自{},区号为{}".format(name,city['name'],city["phone"]))

    return name,city


def calculate_MA(price_list,days = 20):
    if(days <1):
        return None,'无效天数'
    if(len(price_list) < days):
        return None,'数据不足'

    ma_result = []
    for i in range(len(price_list)):
        # 计算5日均线
        ma = 0
        ma_sum_count = 0
        for j in range(days):
            if (i - j >= 0):
                ma += price_list[i - j]
                ma_sum_count += 1
        ma /= ma_sum_count
        ma_result.append(ma)
    return ma_result,'成功'

def calculate_ATR(klineList:list,days = 20):
    if days < 1:
        return None,'无效天数'
    if len(klineList) < days:
        return None,'数据不足'

    range_list = []
    for i in range(len(klineList)):
        range_list.append( round(max(klineList[i]['high'],klineList[i]['close']) - min(klineList[i]['low'],klineList[i]['close']),2) )

    ATR_list= []
    if len(range_list) >0:
        ATR_list = calculate_MA(range_list,days)
    return ATR_list,'成功'
#计算阶乘 方法1
def calculate_factorial_method1(number:int):
    if number <1:
        return None
    result = 1
    for i in range( number):
        result *= (i+1)
    return result
#计算阶乘 方法2
def calculate_factorial_method2(number:int):
    if number < 1:
        return None
    if number > 1:
        return number * calculate_factorial__method2(number-1)
    else:
        return 1

if __name__ == '__main__':
    test_func()
    student = test_func_para('张三',23,[123,149,135])
    print(student)
    #参数顺序错误
    # student = test_func_para('张三' , [123,149,135] , 23)
    # student = test_func_para( [123,149,135], 23 , '张三')
    #调用时
    student = test_func_para(name='张三',age=23,score=[123,149,135])
    student = test_func_para(name='张三',score=[123,149,135],age=23)

    #函数默认值
    student = test_func_para(name='张三',score=[123,149,135],age=23,city='北京')

    #演示返回值
    name,city = test_func_return(name = "张三")
    print(name)
    print(city)
    name,city = test_func_return(name = "李四",citycode='BJ')
    print(name)
    print(city)

    # # 演示计算MA函数
    # close_price_list = [12.72, 12.31, 12.25, 12.43, 12.27, 12.16, 12.22, 12.24, 12.36, 12.27, 12.09, 12.05, 11.78,
    #                     11.73, 11.85, 11.8, 12.21, 12.52, 12.44, 12.46, 12.36, 12.54, 12.67, 12.93, 13.66, 13.5, 13.55,
    #                     13.29, 13.37, 13.71, 13.78, 13.93, 14.18, 14.01, 13.99, 13.92, 13.59, 13.59, 13.56, 13.54,
    #                     14.12, 14, 13.75, 13.69, 13.67, 13.99, 13.85, 13.76, 13.88, 14.2, 14.23, 14.29, 14.37, 14.13,
    #                     14.1, 13.74, 13.35, 13.37, 13.54, 14.38, 14.52, 15.12, 14.89, 14.97, 14.94, 14.9, 14.92, 14.99,
    #                     14.45, 14.31, 14.65, 14.25, 14.31, 14.27, 14.13, 14.16, 14.45, 14.3, 14.44, 14.58, 14.81, 14.69,
    #                     14.55, 14.56, 14.68, 14.45, 14.24, 14.41, 14.84, 15.34, 15.38, 15.18, 15.75, 15.71, 15.9, 15.59,
    #                     16.2, 16.25, 16.24, 16.81, 17.22, 17.18, 16.79, 16.7, 16.51, 16.89, 16.42, 16.45, 16.87, 16.88,
    #                     16.66, 16.91, 16.43, 16.26, 16.86, 16.92, 17.15, 16.96, 16.89, 16.65, 16.28, 16.33, 16.33,
    #                     16.32, 16.34, 16.45, 16.41, 15.85, 15.86, 15.59, 15.8, 15.62, 15.47, 15.49, 15.29, 15.36, 15.45,
    #                     15.31, 15.43, 15.6, 15.41, 15.33, 15.66, 15.6, 16.12, 16.13, 16.5, 16.46, 16.55, 16.59, 16.24,
    #                     16.4, 16.3, 16.47, 16.63, 16.57, 16.45, 16.87, 17.18, 17.07, 17.15, 16.66, 16.79, 16.69, 16.99,
    #                     16.76, 16.52, 16.33, 16.39, 16.45, 16, 16.09, 15.54, 13.99, 14.6, 14.63, 14.77, 14.62, 14.5,
    #                     14.79, 14.77, 14.65, 15.03, 15.37, 15.2, 15.24, 15.59, 15.58, 15.23, 15.04, 14.99, 15.11, 14.5,
    #                     14.79, 14.72, 14.69, 15.39, 15.03, 14.45, 14.76, 14.69, 14.68, 14.52, 13.75, 13.41, 12.71,
    #                     12.23, 12.52, 12.15, 12.61, 12.87, 13.06, 13.15, 12.94, 12.8, 12.89, 12.97, 12.61, 12.88, 12.78,
    #                     12.74, 12.79, 12.59, 12.86, 12.87, 12.68, 12.89, 12.99, 13.45, 13.23, 13.23, 13.24, 13.5, 13.52,
    #                     14.02, 13.93, 13.77, 13.69, 13.95, 14, 13.79, 13.63, 13.3, 13.23]
    # #计算MA
    # ma5 = calculate_MA(close_price_list,5)
    # print(ma5)
    # ma10 = calculate_MA(close_price_list,10)
    # print(ma10)
    # ma20 = calculate_MA(close_price_list)
    # print(ma20)
    # # ma5 = calculate_MA(price_list = close_price_list,days=5)
    # # print(ma5)
    # # ma5 = calculate_MA(days=5 , price_list = close_price_list)
    # # print(ma5)


    ##############################################################################################################################
    # #演示计算ATR
    # #准备K线数据
    # import tushare as ts
    # #获取000001历史日K线
    # dayDataFrame = ts.get_hist_data('000001')
    # #要保存日线数据的列表
    # klineList = []
    # #关于python3 中取消了sort函数
    # #help(dayData.sort_values)
    # dayDataFrame = dayDataFrame.sort_values(by=['date'])
    # #print(dayDataFrame)
    # dateList = list((dayDataFrame.index))
    # #dayList = dayDataFrame.to_json(orient = 'split', force_ascii = False)
    # for i in range(0, len(dayDataFrame)):
    #     #print (i, dayDataFrame.iloc[i])
    #     oneDay = {}
    #     oneDay['date'] = dateList[i]
    #     oneDay['high'] = dayDataFrame.iloc[i]['high']
    #     oneDay['low'] = dayDataFrame.iloc[i]['low']
    #     oneDay['close'] = dayDataFrame.iloc[i]['close']
    #     klineList.append(oneDay)
    # print(klineList)
    #
    # print(calculate_ATR(klineList,20))
    ###########################################################################################################
    # #演示计算阶乘
    # print(calculate_factorial_method1(5))
    # print(calculate_factorial_method1(5))