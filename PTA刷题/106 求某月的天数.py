# 输入年份year、月份month，判断该月的天数。闰年：能被4整除但不能被100整除或者能被400整除的年份是闰年。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。对于每组测试，输入两个整数，表示年份year和月份month。
#
# 输出格式:
# 对于每组测试，输出对应年月的天数。
#
# 输入样例:
# 2020 2
# 2020 4
# 输出样例:
# 29
# 30
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

try:
    while True:
        year, month = map(int,input().split())
        if is_leap_year(year) and month == 2:
            print(29)
        elif not is_leap_year(year) and month == 2:
            print(28)
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print(31)
        else:
            print(30)
except EOFError:
    pass