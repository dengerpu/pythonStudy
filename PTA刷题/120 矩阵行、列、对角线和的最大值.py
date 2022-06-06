# 求一个3*3矩阵每行、每列及对角线和的最大值。
#
# 输入格式:
# 在一行输入9个整数。
#
# 输出格式:
# 在一行输出每行、每列及对角线和的最大值。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 3 6 5 9 8 2 1 4 5
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 19
lst = list(map(int, input().split()))
sum_list =[]
# 由于题中固定是3*3的矩阵，所以直接加
result = 0
for i in range(9):
    if i % 3 == 0:
        sum_list.append(result)
        result = 0
        result += lst[i]
    else:
        result += lst[i]
# 主对角线
a = lst[0] + lst[4] + lst[8]
# 副对角线
b = lst[2] + lst[4] + lst[6]
sum_list.append(a)
sum_list.append(b)
print(max(sum_list))