# 随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。
# 如没有10个英文字母，显示信息“not found”
#
# 输入格式:
# 在一行中输入字符串
#
# 输出格式:
# 在一行中输出最左边的10个不重复的英文字母或显示信息“not found"
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# poemp134567
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# not found
# 输入样例2
# 在这里给出一组输入。例如：
#
# This 156is a test example
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# Thisaexmpl
value = input()
str_list = []
value_list = list(value)
for i in value_list:
    if i.isalpha() and i.upper() not in str_list and i.lower() not in str_list:
        str_list.append(i)
if len(str_list) < 10:
    print('not found')
else:
    print(''.join(str_list[0:10]))
    