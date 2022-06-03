# 小明喜欢上了日期的计算。这次他要做的是日期的减1天操作，即求在输入日期的基础上减去1天后的结果日期。
# 例如：日期为2019-10-01，减去1天，则结果日期为2019-09-30。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入1个日期，日期形式为“yyyy-mm-dd”。保证输入的日期合法，而且输入的日期和计算结果都在[1000-01-01，9999-12-31]范围内。
#
# 输出格式:
# 对于每组测试，在一行上以“yyyy-mm-dd”的形式输出结果。
#
# 输入样例:
# 1
# 2019-10-01
# 输出样例:
# 2019-09-30
import datetime

t = int(input())
for i in range(t):
    my_time = input()
    now_time = datetime.datetime.strptime(my_time, '%Y-%m-%d')
    new_time = now_time + datetime.timedelta(days=-1)
    print(str(new_time).split()[0])