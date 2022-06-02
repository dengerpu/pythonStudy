# 已知数组A和B各有m、n个元素，且元素按值非递减排列，现要求把A和B归并为一个新的数组C，且C中的数据元素仍然按值非递减排列。
# 例如，若A=(3，5，8，11)，B=(2，6，8，9，11，15，20)，
# 则C=(2，3，5，6，8，8，9，11，11，15，20)
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 每组测试数据输入两行，其中第一行首先输入A的元素个数m（1≤m≤100），然后输入m个元素。第2行首先输入B的元素个数n（1≤n≤100），然后输入n个元素。
#
# 输出格式:
# 对于每组测试数据。分别输出将A、B合并后的数组C的全部元素。输出的元素之间以一个空格分隔（最后一个数据之后没有空格）。
#
# 输入样例:
# 1
# 4 3 5 8 11
# 7 2 6 8 9 11 15 20
# 输出样例:
# 2 3 5 6 8 8 9 11 11 15 20
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


t = int(input())
for i in range(t):
    m, *lstA = map(int, input().split())
    n, *lstB = map(int, input().split())
    x = 0
    y = 0
    lstC = []
    while x < m and y < n:
        if lstA[x] <= lstB[y]:
            lstC.append(lstA[x])
            x += 1
        else:
            lstC.append(lstB[y])
            y += 1
    while x < m:
        lstC.append(lstA[x])
        x += 1
    while y < n:
        lstC.append(lstB[y])
        y += 1
    print_list(lstC)
