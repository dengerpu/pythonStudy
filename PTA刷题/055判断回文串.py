# 若一个串正向看和反向看等价，则称做回文串。例如：t，abba，xyzyx均是回文串。
# 给出一个长度不超过60的字符串，判断是否是回文串。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每行输入一个长度不超过60的字符串（串中不包含空格）。
#
# 输出格式:
# 对于每组测试数据，判断是否是回文串，若是输出“Yes”，否则输出“No”。引号不必输出。
#
# 输入样例:
# 2
# abba
# abc
# 输出样例:
# Yes
# No
t = int(input())
for i in range(t):
    my_str = input()
    my_str_reverse = my_str[::-1]
    if my_str == my_str_reverse:
        print('Yes')
    else:
        print('No')
