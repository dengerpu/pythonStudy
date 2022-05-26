# 哥德巴赫猜想之一是指一个偶数（2除外）可以拆分为两个素数之和。请验证这个猜想。
# 因为同一个偶数可能可以拆分为不同的素数对之和，这里要求结果素数对彼此最接近。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入1个偶数n（6≤n≤10000）。
#
# 输出格式:
# 对于每组测试，输出两个彼此最接近的素数a、b（a≤b），两个素数之间留1个空格。
#
# 输入样例:
# 2
# 30
# 40
# 输出样例:
# 13 17
# 17 23
def is_sushu(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

t = int(input())
for i in range(t):
    m = int(input())
    sushu_list = []
    for j in range(2, m):
        if is_sushu(j):
            sushu_list.append(j)
    dic = {}  # 目的是为了一层循环实现求和为m
    for j in sushu_list:
        dic[j] = m - j
    result = {}
    for key, value in dic.items():
        if key in sushu_list and value in sushu_list:
            result[key] = value  # 偶数拆分为两个素数的所有结果
    # print(result)  # 一半是重复的，交换律
    min = m  # 相邻素数差值绝对值最小值，先设为m(可以理解为无穷大)
    for key, value in result.items():
        if value - key < min and value > key:  # 里面有重复的，所以不需要遍历完，其实遍历一半就行了
            min = value - key
            a = key
            b = value
    print(a, b)
