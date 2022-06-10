# 编写程序，统计每行字符串中若干整数的和。每行字符串中整数间的分隔符可能有逗号“,”、分号“ ;”和空格，有多少行就求多少行。
#
# 输入格式:
# 任意输入若干行由整数构成的字符串（回车换行），整数间以逗号或空格或分号分隔。测试数确保至少有一行数据，字符串中的整数数据均合法有效。最后以一个回车结束输入。
#
# 输出格式:
# 对应输出原输入串（一行中的字符序列），冒号后输出各个整数之和。
#
# 输入样例:
# 1; 2 ,3
# 2 3; 4
# 10,20 30; 40
#  9
# 输出样例:
# 1; 2 ,3:6
# 2 3; 4:9
# 10,20 30; 40:100
#  9:9
# import re  # 这个模块的函数可以以多个分隔符分开，但在这里不适用，因为有多个空格
# num_list = input()
# num_list = re.split(',|;|  ', num_list)
# print(num_list)
try:
    while True:
        value = input()
        my_string = value.replace(',', ' ').replace(';',' ')
        num_list = list(map(int, my_string.split()))
        result = value + ":" + str(sum(num_list))
        print(result)
except EOFError:
    pass
