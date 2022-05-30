# 莫大侠练成纵横剑法，走上了杀怪路，每次仅出一招。这次，他遇到了一个正方形区域，由n×n个格子构成，每个格子（行号、列号都从1开始编号）中有若干个怪。莫大侠施展幻影步，抢占了一个格子，使出绝招“横扫四方”，就把他上、下、左、右四个直线方向区域内的怪都灭了（包括抢占点的怪）。请帮他算算他抢占哪个位置使出绝招“横扫四方”能杀掉最多的怪。如果有多个位置都能杀最多的怪，优先选择按行优先最靠前的位置。例如样例中位置（1，2）、（1，3），（3，2），（3，3）都能杀5个怪，则优先选择位置（1，2）。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。对于每组测试，第一行输入n（3≤n≤20），第二行开始的n行输入n×n个格子中的怪数（非负整数）。
#
# 输出格式:
# 对于每组测试数据输出一行，包含三个整数，分别表示莫大侠抢占点的行号和列号及所杀的最大怪数，数据之间留一个空格。
#
# 输入样例:
# 1
# 3
# 1 1 1
# 0 1 1
# 1 1 1
# 输出样例:
# 1 2 5
try:
    while True:
        t = int(input())
        for i in range(t):
            n = int(input())
            lst = []
            kill_list = []
            for j in range(n):
                row_list = list(map(int, input().split()))
                lst.append(row_list)
            for x in range(n):
                for y in range(n):
                    result = 0
                    result += sum(lst[x])  # 先求行的和
                    for column_index in range(n):
                        result += lst[column_index][y]
                    result -= lst[x][y]   #多加了一个这个数，所有要减去
                    kill_list.append(result)
            max_num = max(kill_list)
            for i in range(len(kill_list)):
                if max_num == kill_list[i]:
                    if i <= n:
                        print(1, i+1, max_num)
                    else:
                        print((i//n+1), (i+1) % n, max_num)
                    break
except EOFError:
    pass
