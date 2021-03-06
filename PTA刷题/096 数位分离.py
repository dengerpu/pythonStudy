# 输入一个正整数n，要求输出其位数，并分别以正序和逆序输出各位数字。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入一个整数n（int范围内）。
#
# 输出格式:
# 对于每组测试数据，输出n的位数，然后分别以正序和逆序输出各位数字，每两个数据之间用一个逗号“,”分隔。
#
# 输入样例:
# 2
# 12345
# 246
# 输出样例:
# 5,1,2,3,4,5,5,4,3,2,1
# 3,2,4,6,6,4,2
# n = int(input())
# for i in range(n):
#     num = list(input())
#     print(len(num), end=',')
#     print(','.join(num), end=',')
#     print(','.join(reversed(num)))

# 方法二
n = int(input())
for i in range(n):
    num = int(input())
    lst = []  # 存储整数的每一位，逆序
    count = 0
    while num:
        lst.append(str(num%10))
        num = int(num/10)
        count += 1
    print(count, end=',')
    print(','.join(reversed(lst)), end=',')
    print(','.join(lst))