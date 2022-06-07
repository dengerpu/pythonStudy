# 统计字符串列表中每个字母出现的次数。
#
# 编写程序，使用eval()函数读入一个仅包含字符串对象的列表，然后统计该列表中每个字母出现的次数。
# 列表中的字符串对象仅包含小写英文字母。
#
# 输入格式:
# 一个仅包括字符串对象的列表，且全部字符串对象中仅出现小写英文字母。
#
# 输出格式:
# 字母,次数
#
# ...
#
# 字母,次数
#
# (注意按a-z的顺序输出)
#
# 输入样例:
# ["aaab", "cccdz"]
# 输出样例:
# 在这里给出相应的输出。例如：
#
# a,3
# b,1
# c,3
# d,1
# z,1
str_list = eval(input())
chars = [chr(x) for x in range(ord('a'), ord('z')+1)]
counts = [0]*26
for word in str_list:
    for i in word:
        counts[ord(i) - ord('a')] += 1
for word, num in zip(chars, counts):
    if num > 0:
        print("%s,%d" % (word, num))

