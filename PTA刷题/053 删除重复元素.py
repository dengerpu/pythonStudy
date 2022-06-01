# 对于给定的数列，要求把其中的重复元素删去再从小到大输出。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据先输入一个整数n（1≤n≤100），再输入n个整数。
#
# 输出格式:
# 对于每组测试，从小到大输出删除重复元素之后的结果，每两个数据之间留一个空格。
#
# 输入样例:
# 1
# 10 1 2 2 2 3 3 1 5 4 5
# 输出样例:
# 1 2 3 4 5
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


t = int(input())
for i in range(t):
    lst = list(map(int, input().split()))
    my_list = []
    for j in range(1,len(lst)):
        if lst[j] not in my_list:
            my_list.append(lst[j])
    my_list.sort()
    print_list(my_list)

