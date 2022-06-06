# 输入n（1<n<100）个整数到一个数组中，使得其中最小的一个数成为数组的第一个元素（首元素）。若有多个最小者，则首元素仅与最早出现的最小者交换。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据的第一行输入n(1<n<100)，第二行输入n个整数。
#
# 输出格式:
# 对于每组测试，输出将这n个整数中最小的数与第一个数对换后的n个整数。
#
# 输入样例:
# 5
# 5 3 4 1 2
# 输出样例:
# 1 3 4 5 2
def print_list(lst, n):
    for i in range(n):
        if i != n-1:
            print(lst[i], end=' ')
        else:
            print(lst[i])

try:
    while True:
        n = int(input())
        lst = list(map(int, input().split()))
        min_num = min(lst)
        for i in range(n):
            if lst[i] == min_num:
                lst[0], lst[i] = lst[i], lst[0]
                break
        print_list(lst, n)
except EOFError:
    pass