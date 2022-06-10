# 输入一个字符串，本题要求滤去所有的非十六进制字符（不分大小写），组成一个新的表示十六进制数字的字符串，然后将其转换为十进制数后输出。如果在第一个十六进制字符之前存在字符“-”，则代表该数是负数。如果没有十六进制字符，不输出任何信息;-0和0都输出为0。
#
# 输入格式:
# 输入一行非空字符串。
#
# 输出格式:
# 在一行中输出转换后的十进制数，或没有任何输出。
#
# 输入样例1:
# +-P-xf4+-1!
# 输出样例1:
# -3905
# 输入样例2:
# +-nn*)+-lp
# 输出样例2:
#
import math
value = input()
hex_string = ''
for i in value:
    if '0' <= i <= '9' or 'a' <= i <= 'f' or 'A' <= i <= 'F':
        hex_string += i
if hex_string != '':
    index = value.find(hex_string[0])
    hex_string = hex_string[::-1]
    #  hex函数可以将十进制转换为十六进制
    hex_string_list = list(hex_string)
    sum = 0
    for i in range(len(hex_string_list)):
        if hex_string_list[i] == 'a' or hex_string_list[i] == 'A':
            a = 10
        elif hex_string_list[i] == 'b' or hex_string_list[i] == 'B':
            a = 11
        elif hex_string_list[i] == 'c' or hex_string_list[i] == 'C':
            a = 12
        elif hex_string_list[i] == 'd' or hex_string_list[i] == 'D':
            a = 13
        elif hex_string_list[i] == 'e' or hex_string_list[i] == 'E':
            a = 14
        elif hex_string_list[i] == 'f' or hex_string_list[i] == 'F':
            a = 15
        else:
            a = int(hex_string_list[i])
        sum += a * int(math.pow(16,i))
    if value[:index].find('-') != -1:
        sum = -sum
    print(sum)
else:
    pass