# 从键盘输入任意字符串，查找字符串中的所有数字字符串。若无数字字符串，则输出“No digits"，若有数字子串，则找到所有数字子串并求它们的和。
# 注意：数字可能有实数的子串。
#
# 输入格式:
# 输入任意字符串。
#
# 输出格式:
# 若无数字字符串，则输出“No digits"，若有数字子串，则找到所有数字子串并求它们的和。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 34euitye87.89df37.903jdhf374
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 533.793
import re
value = input()
num_list = re.findall(r"-?\d+\.?\d*", value)
num_list = [eval(x) for x in num_list]
if num_list:
    print(sum(num_list), end='')
else:
    print('No digits', end='')