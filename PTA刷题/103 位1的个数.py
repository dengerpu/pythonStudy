# 输入一个非负整数，求它变成二进制后1的个数（提示：用bin函数）。
#
# 输入格式:
# 输入一个正整数。
#
# 输出格式:
# 输出1的个数。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# 37
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# 3
# 输入样例2:
# 在这里给出一组输入。例如：
#
# 0
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# 0
n = int(input())
bin_n = bin(n)
# count = 0
# for i in bin_n:
#     if i == '1':
#         count += 1
# print(count)
count = 0
for i in range(0, 32):  # 这种写法适用于c语言
    if (n >> i) & 1 == 1:  # 左移，按位与（两个都为1才为1 ）
        count += 1
print(count)