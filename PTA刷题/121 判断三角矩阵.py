# 本题要求编写程序，判断一个给定的方阵是否是三角矩阵。三角矩阵包含上三角矩阵和下三角矩阵两种。
#
# 上三角矩阵指主对角线以下的元素都为0的矩阵；下三角矩阵指主对角线以上的元素都为0的矩阵；主对角线为从矩阵的左上角至右下角的连线。
#
# 输入矩阵是三种情况之一(上三角矩阵、下三角矩阵或都不是)。
#
# 输入格式:
# 输入第一行给出一个正整数T，为待测矩阵的个数。接下来给出T个矩阵的信息：每个矩阵信息的第一行给出一个不超过10的正整数n。随后n行，每行给出n个整数，其间以空格分隔。
#
# 输出格式:
# 每个矩阵的判断结果占一行。如果输入的矩阵是上三角矩阵，输出“upper triangular matrix”，如果输入的矩阵是下三角矩阵，输出“lower triangular matrix”，都不是输出“no”。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 3
# 3
# 1 2 3
# 0 4 5
# 0 0 6
# 2
# 1 0
# -8 2
# 4
# 1 2 4 0
# 56 5 7 9
# 3 4 8 9
# 0 0 0 0
# 输出样例:
# 在这里给出相应的输出。例如：
#
# upper triangular matrix
# lower triangular matrix
# no
t = int(input())
for i in range(t):
    n = int(input())
    lst = []
    for j in range(n):
        lst.append(list(map(int, input().split())))
    flag_upper = 1
    flag_lower = 1
    for x in range(n):
        for y in range(n):
            if x < y and lst[x][y] != 0:  # 右上角
                flag_lower = 0
            if x > y and lst[x][y] != 0:  # 左下角
                flag_upper = 0
    if flag_upper:
        print('upper triangular matrix')
    elif flag_lower:
        print('lower triangular matrix')
    else:
        print('no')
