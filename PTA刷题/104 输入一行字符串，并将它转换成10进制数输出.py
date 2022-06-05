# 输入一行字符串，去掉非16进制字符，并将它转换成10进制数输出。
#
# 输入格式:
# 输入一行字符串。
#
# 输出格式:
# 输出16进制字符串和转换后的10进制数。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# _ahg1*B
# 输出样例:
# 在这里给出相应的输出。例如：
#
# a1B
# 2587
import binascii
import math

value = input()
my_string = ''
for i in value:
    if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 70 or 97 <= ord(i) <= 102:
        my_string += i
print(my_string)
#  hex函数可以将十进制转换为十六进制
string_list = list(my_string)
sum = 0
for i in range(len(string_list)):
    if string_list[i] == 'a' or string_list[i] == 'A':
        a = 10
    elif string_list[i] == 'b' or string_list[i] == 'B':
        a = 11
    elif string_list[i] == 'c' or string_list[i] == 'C':
        a = 12
    elif string_list[i] == 'd' or string_list[i] == 'D':
        a = 13
    elif string_list[i] == 'e' or string_list[i] == 'E':
        a = 14
    elif string_list[i] == 'f' or string_list[i] == 'F':
        a = 15
    else:
        a = int(string_list[i])
    sum += a * int(math.pow(16,len(string_list)-1-i))
print(sum)