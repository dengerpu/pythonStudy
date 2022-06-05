# 输入一个正整数，求其各个数位上的数字之和。例如，输入12345，输出15。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个正整数n（int范围内）。
#
# 输出格式:
# 对于每组测试，输出每个n对应的各位数字和。
#
# 输入样例:
# 12345
# 输出样例:
# # 15
# try:
#     while True:
#         lst = list(input())
#         lst = [int(x) for x in lst]
#         print(sum(lst))
# except EOFError:
#     pass

# 方法二：
try:
    while True:
        n = int(input())
        sum = 0
        while n:
            sum += n % 10
            n = int(n / 10)
        print(sum)
except EOFError:
    pass