# 输入一行字符，以回车结束，统计其中单词的个数。单词是中间没有空格的字符序列，各单词之间用空格分隔，单词间空格数可以是多个。
#
# 输入格式:
# 在一行中输入字符
#
# 输出格式:
# 在一行中输出单词的数量
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# Let's  go   to room  209
# 输出样例:
# 在这里给出相应的输出。例如：
#
# count = 5
# my_str = input()
# str_list = my_str.split()
# print(f'count = {len(str_list)}')
print(f'count = {len(input().split())}')
