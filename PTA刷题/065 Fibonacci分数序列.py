# 求Fibonacci分数序列的前n项之和。Fibonacci分数序列的首项为2/1，后面依次是：3/2，5/3，8/5，13/8，21/13……
#
# 输入格式:
# 测试数据由多组，处理到文件尾。每组测试输入一个正整数n（2≤n≤20）。
#
# 输出格式:
# 对于每组测试，输出Fibonacci分数序列的前n项之和。结果保留6位小数。
#
# 输入样例:
# 3
# 8
# 15
# 输出样例:
# 5.166667
# 13.243746
# 24.570091
try:
    while True:
        n = int(input())
        count = 0
        a = 2
        b = 1
        result = 0
        while count < n:
            result += a/b
            t = a
            a = a+b
            b = t
            count += 1
        print('%.6f' % result)
except EOFError:
    pass

