# 输入一些小于10的非负整数，求这些数组成的最大整数，要求各位数字互不相同。
#
# 输入格式:
# 用空格分隔输入一些小于10的非负整数，要求每个整数x符合条件：0⩽x<10
#
# 输出格式:
# 输出一个整数，由输入的数组成的最大整数，且每位数字各不相同。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 3 1 1 1 1 3 9 4 4
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 9431
num_list = input().split()
number_list = []
for i in range(9, -1, -1):  # 生成[9,0]
    number_list.append(str(i))
number_str = ''
for i in number_list:
    if i in num_list:
        number_str += i
print(number_str)