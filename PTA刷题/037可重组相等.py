# 如果一个字符串通过字符位置的调整能重组为另一个字符串，就称这两个字符串“可重组相等”。给出两个字符串，请判断它们是否“可重组相等”。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入两字符串s和t。
#
# 输出格式:
# 对于每组测试，判断它们是否“可重组相等”，是则输出“Yes”，否则输出“No”。注意，引号不必输出。
#
# 输入样例:
# 1
# Oh, yes!
# y! O,seh
# 输出样例:
# Yes
n = int(input())
for i in range(n):
    str_list = list(input())
    reverse_str_list = list(input())
    str_list.sort()
    reverse_str_list.sort()
    if str_list == reverse_str_list:
        print('Yes')
    else:
        print('No')
