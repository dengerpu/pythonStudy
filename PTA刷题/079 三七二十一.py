# 某天，诺诺看到三七二十一（3721）数，觉得很神奇，这种数除以3余2，而除以7则余1。例如8是一个3721数，因为8除以3余2，8除以7余1。现在给出两个整数a、b，求区间[a，b]中的所有3721数，若区间内不存在3721数则输出“none”。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入两个整数a，b（1≤a<b<2000）。
#
# 输出格式:
# 对于每组测试，在一行上输出区间[a，b]中所有的3721数，每两个数据之间留一个空格。如果给定区间不存3721数，则输出“none”（引号不必输出）。
#
# 输入样例:
# 2
# 1 7
# 1 100
# 输出样例:
# none
# 8 29 50 71 92
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    lst = []
    for j in range(a, b+1):
        if j % 3 == 2 and j % 7 == 1:
            lst.append(j)
    if len(lst):
        print_list(lst)
    else:
        print('none')