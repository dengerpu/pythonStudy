# 读入 1 个正整数 n(3≤n<9)和 1 个整数 digit（2<=digit<=9）, 请输出一个 n 阶的方阵, 该矩阵所有边上的元素都是 digit, 其它元素都是 digit-1.
#
# 输入格式:
# 在一行中输入n和digt
#
# 输出格式:
# 输出n 阶的方阵
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 4   2
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 2 2 2 2
# 2 1 1 2
# 2 1 1 2
# 2 2 2 2
value = input()
n, digt = value.split()
try:
    n = int(n)
    digt = int(digt)
    if n < 3 or n >= 9 or digt < 2 or digt > 9:  # 由于题中并没有涉及异常处理的说明（此处是我自己添加）
        raise Exception
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1:
                print(digt, end=' ')
            elif j != 0 and j != n-1:
                print(digt-1, end=' ')
            else:
                print(digt, end=' ')
        print()  # 换行
except Exception as e:
    print(e)
