# 输入n个数，然后把这n个数逆序输出。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据在一行上首先输入整数n，接着输入n（n<=40）个整数。
#
# 输出格式:
# 对于每组测试，逆序输出n个数，每两个数据之间留一个空格。每两组测试数据之间留一个空行。
#
# 输入样例:
# 5 1 2 3 4 5
# 3 1 2 3
# 输出样例:
# 5 4 3 2 1
#
# 3 2 1
flag = 1


def print_list(lst, n):
    global flag
    if flag:
        print(end='')
        flag = 0
    else:
        print()
    for i in range(n):
        if i != n - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


try:
    while True:
        n, *lst = map(int, input().split())
        lst = lst[::-1]
        print_list(lst, n)
except EOFError:
    pass