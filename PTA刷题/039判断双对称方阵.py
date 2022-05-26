# 对于一个n阶方阵，请判断该方阵是否双对称，即既左右对称又上下对称。若是则输出“yes”，否则输出“no”。例如，样例中，以第2列为界则左右对称，以第2行为界则上下对称，因此输出“yes”。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组数据的第一行输入方阵的阶n（2≤n≤50），接下来输入n行，每行n个整数，表示方阵中的元素。
#
# 输出格式:
# 对于每组测试数据，若该方阵双对称，则输出“yes”，否则输出“no”。注意，引号不必输出。
#
# 输入样例:
# 2
# 3
# 1 2 1
# 3 5 3
# 1 4 1
# 3
# 1 2 1
# 3 5 3
# 1 2 1
# 输出样例:
# no
# yes
t = int(input())
for i in range(t):
    n = int(input())
    lst = []
    flag = 0  # 永安里标记是否对称
    for i in range(n):
        lst.append(input().split())
    k = int(n/2)
    for i in range(k):  # 先判断上下是否对称,由于是方阵，这里就不用len(lst)直接用n
        if lst[i] != lst[n-i-1]:
            flag = 1
            break
    if flag != 1:  # 上下对称再判断左右对称
        for item_list in lst:
            for j in range(k):
                if item_list[i] != item_list[n-i-1]:
                    flag = 1
                    break
    if flag == 0:
        print('yes')
    else:
        print('no')


