# 判断两个由大小写字母和空格组成的字符串在忽略大小写，且忽略空格后是否含有完全相同的字母。
#
# 输入格式:
# 两行，输入两个由大小写字母和空格组成的字符串
#
# 输出格式:
# 若两个字符串含有完全相同的字母(不区分大小写)，输出YES，否则输出NO。
#
# 输入样例1:
# This is a pencil
# this is an apple
# 输出样例1:
# NO
# 输入样例2:
# Hello World
# hello word
# 输出样例2:
# YES
string1 = input().replace(' ', '').lower()
string2 = input().replace(' ', '').lower()
string3 = ''  # 用于去重
string4 = ''
for i in string1:
    if i not in string3:
        string3 += i
for i in string2:
    if i not in string4:
        string4 += i
if string3 == string4:
    print('YES', end='')
else:
    print('NO', end='')