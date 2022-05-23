# 编写程序，用于计算有n(1<n<10)个字符串中最长的字符串的长度。前导空格不要计算在内！
#
# 输入格式:
# 在第一行中输入n,接下的每行输入一个字符串
#
# 输出格式:
# 在一行中输出最长的字符串的长度
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 4
#         blue
# yellow
# red
# green
# 输出样例:
# 在这里给出相应的输出。例如：
#
# length=6
n = int(input())
str_list = []
for i in range(n):
    value = input()
    str_list.append(value.strip())  # 去掉左右空格
str_length_list = [len(x) for x in str_list]
print(f'length={max(str_length_list)}')
