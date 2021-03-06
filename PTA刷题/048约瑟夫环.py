# 有n个人围成一圈（编号为1～n），从第1号开始进行1、2、3报数，凡报3者就退出，下一个人又从1开始报数……直到最后只剩下一个人时为止。请问此人原来的位置是多少号?
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数n（5≤n≤100）。
#
# 输出格式:
# 对于每组测试，输出最后剩下那个人的编号。
#
# 输入样例:
# 10
# 28
# 69
# 输出样例:
# 4
# 23
# # 68
try:
    while True:
        n = int(input())
        lst = [0 for i in range(0, n+1)]
        length = len(lst) - 1  # 减一是因为要去掉0这个索引
        i = 1
        k = 0
        while length > 1:
            if lst[i] != -1:
                k += 1
            if k == 3:
                lst[i] = -1
                k = 0
                length -= 1
            i += 1
            if i == n+1:
                i = 1
        for x in range(1, n+1):
            if lst[x] == 0:
                print(x)
except EOFError:
    pass