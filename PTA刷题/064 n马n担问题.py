# 有n匹马，驮n担货，大马驮3担，中马驮2担，两匹小马驮1担，问有大、中、小马各多少匹? （某种马的数量可以为0）
#
# 输入格式:
# 测试数据由多组，处理到文件尾。每组测试输入一个正整数n（8≤n≤1000）。
#
# 输出格式:
# 对于每组测试，逐行输出所有符合要求的大、中、小马的匹数。要求按大马数从小到大的顺序输出，每两个数字之间留一个空格。
#
# 输入样例:
# 20
# 输出样例:
# 1 5 14
# 4 0 16
try:
    while True:
        n = int(input())
        for i in range(n+1):  # 为减少时间复杂度，采用双层循环
            for j in range(n+1):
                if i*3 + j*2 + (n-i-j)/2 == n:
                    print(i, j, n-i-j)
except EOFError:
    pass