# 在一行上输入若干整数，每个整数以一个空格分开，求这些整数的平均值。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入一个字符串（仅包含数字字符和空格）。
#
# 输出格式:
# 对于每组测试，输出以空格分隔的所有整数的平均值，结果保留一位小数。
#
# 输入样例:
# 1
# 1 2 3 4 5 6 7 8 9 10
# 输出样例:
# 5.5
n = int(input())
aver_list = []
for i in range(n):
    result = 0
    lst = input().split()
    for item in lst:
        result += float(item)
    aver = result / len(lst)
    print('%.1f' % aver)
