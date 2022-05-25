# 在一行上输入两个字符串s和英文字符串t，要求在s中查找t。其中，字符串s，t均不包含空格，且长度均小于80。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入2个长度不超过80的字符串s和t（s和t都不包含空格）。
#
# 输出格式:
# 对于每组测试数据，若在s中找到t，则输出“Found!”，否则输出“not Found!”。引号不必输出。
#
# 输入样例:
# 2
# dictionary lion
# factory act
# 输出样例:
# not Found!
# Found!
# n = int(input())
# my_dict = {}
# for i in range(n):
#     s, t = input().split()
#     my_dict[s] = t
# for key, value in my_dict.items():
#     # if key.find(value) != -1:
#     if value in key:
#         print('Found!')
#     else:
#         print('not Found!')

n = int(input())  # 这上面的题太不标准了（也可能是我理解有问题，我上面的理解是全部输入完之后再进行输入，可是提交答案错误）
for i in range(n):
    s, t = input().split()
    if s.find(t) != -1:
        print('Found!')
    else:
        print('not Found!')