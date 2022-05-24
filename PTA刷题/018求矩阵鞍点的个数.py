# 一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小。
#
# 本题要求编写程序，求一个给定的n阶方阵的鞍点。
#
# 输入格式：
# 输入第一行给出一个正整数n（1≤n≤6）。随后n行，每行给出n个整数，其间以空格分隔。
#
# 输出格式：
# 鞍点的个数
#
# 输入样例1：
#
# 4
# 1 7 4 1
# 4 8 3 6
# 1 6 1 2
# 0 7 8 9
# 输出样例1：
#
# 1
# 输入样例2：
#
# 2
# 1 7
# 4 1
# 输出样例2：
#
# 0
# 输入样例3：
#
# 3
# 4    7    8
# 1    3    3
# 2    3    1
# 输出样例3：
#
# 2
n = int(input())
my_list = []
count = 0
for i in range(n):
    my_list.append(list(map(int, input().split())))  # 每行信息以一个列表存储在my——list列表中
for i in range(n):
    column_list = []  # 为什么要用数组，不直接用一个变量存储，因为会存在相等的最值
    row_max = max(my_list[i])  # 求出每行的最大值
    for j in range(n):
        if my_list[i][j] == row_max:
           column_list.append(j)  # 最大值所在的列
    for j in range(len(column_list)):
        for k in range(n):
            if my_list[k][column_list[j]] < row_max:
                break  # 说明不是该行的最小值
        else:
            count += 1
print(count)


