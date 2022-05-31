# 输入一个整数n及一个n阶方阵，判断该方阵是否以主对角线对称，输出“Yes”或“No”。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组数据的第一行输入一个整数n（1<n<100），接下来输入n阶方阵（共n行，每行n个整数）。
#
# 输出格式:
# 对于每组测试，若该方阵以主对角线对称，则输出“Yes”，否则输出“No”。引号不必输出。
#
# 输入样例:
# 1
# 4
# 1 2 3 4
# 2 9 4 5
# 3 4 8 6
# 4 5 6 7
# 输出样例:
# Yes
t = int(input())
for i in range(t):
    n = int(input())
    lst = []
    for j in range(n):
        lst.append(list(map(int, input().split())))
    flag = 1
    for x in range(n):
        for y in range(x+1):
            if lst[x][y] != lst[y][x]:
                flag = 0
                break
    result = 'Yes' if flag else 'No'
    print(result)

