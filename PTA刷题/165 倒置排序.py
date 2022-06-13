# 将一些整数按倒置值从小到大排序后输出。倒置是指把整数的各个数位倒过来构成一个新数，例如：13倒置成了31。若倒置值相同则按原数的从小到大排序，例如130和13，倒置数都是31，则13排在130前面。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试先输入一个整数n（n≤80），然后输入n个非负整数。
#
# 输出格式:
# 对于每组测试，结果占一行，输出排序后的结果，数据之间留一个空格。
#
# 输入样例:
# 2
# 4 83 13 24 36
# 4 99 100 123 12345
# 输出样例:
# 13 83 24 36
# 100 99 123 12345
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


t = int(input())
for i in range(t):
    n, *lst = map(int, input().split())
    lst = [(str(x)[::-1]) for x in lst]  # 逆置，逆置后进行排序
    lst.sort(key=lambda x: (int(x), len(x)))  # 多关键字排序，如果大小相同就按位数来排
    lst = [(str(x)[::-1]) for x in lst]  # 再逆置回来
    lst = [int(x) for x in lst]
    print_list(lst)