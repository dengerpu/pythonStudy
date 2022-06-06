# 输入两个整数n和m，再输入n个整数构成一个数列，把前m个数循环移位到数列的右边。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据第一行输入2个正整数n、m（1<=m，n<100），第二行输入n个整数。
#
# 输出格式:
# 对于每组测试数据, 在一行上输出把前m个数循环移位到数列的右边后的数列，每两个数据之间留一个空格。
#
# 输入样例:
# 5 3
# 1 2 3 4 5
# 输出样例:
# 4 5 1 2 3
def move_list(lst, n):
    a = lst[0]
    for i in range(n -1):
        lst[i] = lst[i+1]
    lst[n-1] = a


def print_list(lst, n):
    for i in range(n):
        if i != n-1:
            print(lst[i], end=' ')
        else:
            print(lst[i])

try:
    while True:
        n, m = map(int, input().split())
        lst = list(map(int, input().split()))
        for i in range(m):
            move_list(lst, n)
        print_list(lst, n)
except EOFError:
    pass
