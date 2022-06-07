# 输入一组单词在字典中的页码。而后得出多个单词在字典中的页码分别是多少。
#
# 输入格式:
# 首先输入的是一组单词及其在字典中的页码。其中，第一行一个整数 N，表示字典中一共有多少单词(N≤20000)。接下来每两行表示一个单词，其中： 两行中的第 1 行是一个长度≤100 的字符串，表示这个单词，全部字母小写，单词不会重复。两行中的第 2 行是一个整数，表示这个单词在字典中的页码。
#
# 接下来输入的是要查询页码的单词。其中的第一行是一个整数 M，表示要查的单词数(M≤10000)。 接下来 M 行，每行一个字符串，表示要查的单词，保证在字典中存在。
#
# 输出格式:
# M 行，每行一个整数，表示第 i 个单词在字典中的页数。
#
# 输入样例:
# 4
# cungneh
# 19
# wyd
# 17
# aqkj
# 2
# olckomm
# 15
# 4
# wyd
# aqkj
# cungneh
# olckomm
# 输出样例:
# 17
# 2
# 19
# 15
n = int(input())
my_dict = {}
for i in range(n):
    word = input()
    page_num = int(input())
    my_dict[word] = page_num
n = int(input())
for i in range(n):
    search = input()
    for key in my_dict:
        if key == search:
            print(my_dict[key])