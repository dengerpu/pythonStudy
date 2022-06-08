# Write a program to calculate the length of the longest string with n(1<n<10) strings. The leading space is not counted!
#
# input format:
# Enter n in the first line which indicate that there are n strings to be entered, each string taking up one line.
#
# output format:
# Output the length of the longest string
#
# input sample:
# 4
#         blue
# yellow
# red
# green
# output sample:
# length=6
n = int(input())
lst = []
for i in range(n):
    word = input().lstrip()  # 去除字符串左边的空格
    lst.append(len(word))
print(f'length={max(lst)}')
