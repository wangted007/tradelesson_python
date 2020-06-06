
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
