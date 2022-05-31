# 给定一个n行m列的矩阵，请找出最大数与最小数并交换它们的位置。若最大或最小数有多个，以最前面出现者为准（矩阵以行优先的顺序存放，请参照样例）。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据的第一行输入2个整数n，m（1<n，m<20），接下来输入n行数据，每行m个整数。
#
# 输出格式:
# 对于每组测试数据，输出处理完毕的矩阵（共n行，每行m个整数），每行中每两个数据之间留一个空格。具体参看输出样例。
#
# 输入样例:
# 3 3
# 4 9 1
# 3 5 7
# 8 1 9
# 输出样例:
# 4 1 9
# 3 5 7
# 8 1 9
try:
    while True:
        n, m = map(int, input().split())
        lst = []
        for i in range(n):
            lst += map(int, input().split())
        min_num = min(lst)
        flag1 = 1
        max_num = max(lst)
        flag2 = 1
        for i in range(len(lst)):
            if lst[i] == min_num and flag1:
                min_index = i
                flag1 = 0
            if lst[i] == max_num and flag2:
                max_index = i
                flag2 = 0
        lst[max_index], lst[min_index] = lst[min_index], lst[max_index]
        for i in range(len(lst)):
            if (i+1) % m == 0:
                print(lst[i])
            else:
                print(lst[i], end=' ')
except EOFError:
    pass