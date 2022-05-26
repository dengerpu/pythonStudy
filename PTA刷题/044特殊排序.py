# 7-44 特殊排序
# 作者 usx程序设计类课程组
# 单位 绍兴文理学院
# 输入一个整数n和n个各不相等的整数，将这些整数从小到大进行排序，要求奇数在前，偶数在后。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试先输入一个整数n（1<n<100），再输入n个整数。
#
# 输出格式:
# 对于每组测试，在一行上输出根据要求排序后的结果，数据之间留一个空格。
#
# 输入样例:
# 3
# 5 1 2 3 4 5
# 3 12 4 5
# 6 2 4 6 8 0 1
# 输出样例:
# 1 3 5 2 4
# 5 4 12
# 1 0 2 4 6 8
t = int(input())
for i in range(t):
    lst = list(map(int, input().split()))
    # 题中要求是每组数据输入前，先输入n,再输入n个整数
    lst.pop(0)
    lst.sort()
    lst.sort(key=lambda x: x % 2 == 0)
    for i in range(len(lst)):
        if i != len(lst)-1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


