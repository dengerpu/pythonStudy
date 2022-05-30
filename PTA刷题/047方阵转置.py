# 输入一个n×n的方阵，把其转置并输出。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。对于每组测试，第一行输入一个整数n（n≤10），接下来的n行每行输入n个不超过2位的整数。
#
# 输出格式:
# 对于每组测试，输出这n×n矩阵的转置方阵，每行的每两个数据之间留一个空格。
#
# 输入样例:
# 5
# 5 51 96 80 45
# 51 57 77 45 47
# 72 45 58 83 21
# 0 28 42 72 42
# 91 61 7 73 66
# 输出样例:
# 5 51 72 0 91
# 51 57 45 28 61
# 96 77 58 42 7
# 80 45 83 72 73
# 45 47 21 42 66
try:
    while True:
        n = int(input())
        lst = []
        for i in range(n):
            row_list = input().split()
            lst.append(row_list)
        for i in range(n):
            for j in range(i+1):
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
        for i in range(n):
            for j in range(n):
                if j != n-1:
                    print(lst[i][j], end=' ')
                else:
                    print(lst[i][j])
except EOFError:
    pass
