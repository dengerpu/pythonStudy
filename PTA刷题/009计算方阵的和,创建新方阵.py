# 输入 1 个正整数 n(1≤n)，再按行读入 n 阶方阵 a 和 b, 生成并输出 n 阶方阵 c，c 中的元素是 a 和 b 对应元素的和.
# c[i][j]=a[i][j]+b[i][j] i,j=0,1,2...n-1（1<=c[i]<=99)
#
# 输入格式:
# 在第一行输入n
# 在第二行输入a方阵
# 在第一行输入b方阵
#
# 输出格式:
# 输出c方阵
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 3
# 1 2 3 4 5 6 7 8 9
# 2 3 4 5 6 7 8 9 1
# 输出样例:
# 在这里给出相应的输出。例如：
#
#  3  5  7
#  9 11 13
# 15 17 10
n = int(input())
a_matrix = input()
b_matrix = input()
a_list = a_matrix.split()
b_list = b_matrix.split()
a_list = [int(x) for x in a_list]  # 字符串转换为整数
b_list = [int(x) for x in b_list]
martix_list = []  # 存储方阵元素列表
for i, j in zip(a_list, b_list):
    martix_list.append(i+j)

for i in range(n):
    for j in range(n):
        if martix_list[j + i*n] < 10:
            print(end=' ')  # 小于10 前面输入空格，保证美观
        print(martix_list[j + i*n], end=' ')
    print()  # 换行

