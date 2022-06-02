# 输入n个整数，把第i个到第j个之间的全部元素进行逆置，并输出逆置后的n个数。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试先输入三个整数n，i，j（0 < n <= 100，1 ≤ i < j ≤ n），再输入n个整数。
#
# 输出格式:
# 对于每组测试数据，输出逆置后的n个数，要求每两个数据之间留一个空格。
#
# 输入样例:
# 1
# 7 2 6 11 22 33 44 55 66 77
# 输出样例:
# 11 66 55 44 33 22 77
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


t = int(input())
for i in range(t):
    n, i, j, *lst = map(int, input().split())
    lst[i-1:j] = reversed(lst[i-1:j])  # reversed 函数返回一个反转的迭代器。
    print_list(lst)