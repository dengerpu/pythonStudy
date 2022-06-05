# 求n个非负整数x1, x2 …… xn（xi为第i个元素）的均方差，公式如下：
#
# 均方差 s = 整体根号下 （（x1-avg）的平方 + （x2 - avg）的平方 + ..（xn-avg）的平方）  / n
# avg是平均数
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据先输入一个整数n（1≤n≤100），再输入n个整数xi（0≤xi≤1000）。
#
# 输出格式:
# 对于每组测试数据，在一行上输出均方差，结果保留5位小数。
#
# 输入样例:
# 2
# 4 6 7 8 9
# 10 6 3 7 1 4 8 2 9 11 5
# 输出样例:
# 1.11803
# 3.03974
import math

t = int(input())
for i in range(t):
    n, *lst = (map(int, input().split()))
    avg = sum(lst) / n
    result = 0
    for x in lst:
        result += (x-avg)*(x-avg)
    s = math.sqrt(result/n)
    print(f'{s:.5f}')
