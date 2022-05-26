# 如果矩阵A中存在这样的一个元素A[i][j]满足下列条件：A[i][j]是第i行中值最小的元素，且又是第j列中值最大的元素，则称之为该矩阵的一个马鞍点。请编写程序求出矩阵A的马鞍点。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 对于每组测试数据，首先输入2个正整数m、n（1 ≤ m，n ≤ 100），分别表示二维数组的行数和列数。
# 然后是二维数组的信息，每行数据之间用一个空格分隔，每个数组元素均在int型范围内。简单起见，假设二维数组的元素各不相同，且每组测试数据最多只有一个马鞍点。
#
# 输出格式:
# 对于每组测试数据，若马鞍点存在则输出其值，否则输出“Impossible”。注意，引号不必输出。
#
# 输入样例:
# 1
# 4 3
# 6 7 11
# 2 17 13
# 4 -2 3
# 5 9 88
# 输出样例:
# 6
# t = int(input())
# for i in range(t):
#     m, n = map(int, input().split())
#     lst = []
#     for j in range(m):
#         lst.append(list(map(int, input().split())))
#     count = 0  # 记录鞍点的个数
#     for i in range(m):
#         column_list = []  # 用数组存储列的索引的原因，会存在相等的最值
#         row_min = min(lst[i])  # 行上的最小值
#         for j in range(n):
#             if lst[i][j] == row_min:
#                 column_list.append(j)  # 最小值所在列
#         for min_column_index in column_list:
#             for z in range(m):
#                 if lst[z][min_column_index] > row_min:
#                     break   # 说明不是该列的最大值
#             else:
#                 count += 1
#     if count == 0:
#         print('Impossible')
#     else:
#         print(count)
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    lst = []
    for j in range(m):
        lst.append(list(map(int, input().split())))
    count = 0  # 记录鞍点的个数
    for i in range(m):
        # column_list = []  # 用数组存储列的索引的原因，会存在相等的最值,由于是不同的值，所以不需要用列表

        row_min = min(lst[i])  # 行上的最小值
        for j in range(n):
            if lst[i][j] == row_min:
                # column_list.append(j)  # 最小值所在列
                column_index = j  # 最小值的列
        for k in range(m):
            if lst[k][column_index] > row_min:
                break  # 说明该数不是改列的最大值
        else:
            point = row_min
            count += 1

        # for min_column_index in column_list:  此处代码为存在多个相等最值情况，此题可以忽略
        #     for z in range(m):
        #         if lst[z][min_column_index] > row_min:
        #             break   # 说明不是该列的最大值
        #     else:
        #         count += 1
    if count == 0:
        print('Impossible')
    else:
        print(point)