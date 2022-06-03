# 输入两个3位的正整数m，n，输出[m，n]区间内所有的“水仙花数”。所谓“水仙花数”是指一个3位数，其各位数字的立方和等于该数本身。
#
# 输入格式:
# 测试数据由多组，处理到文件尾。每组测试输入两个3位的正整数m，n（100≤m<n≤999）。
#
# 输出格式:
# 对于每组测试，若[m，n]区间内没有水仙花数则输出“none”（引号不必输出），否则逐行输出区间内所有的水仙花数，每行输出的格式具体参看输出样例。
#
# 输入样例:
# 100 150
# 100 200
# 输出样例:
# none
# 153=1*1*1+5*5*5+3*3*3
try:
    while True:
        m, n = map(int, input().split())
        flag = 1
        for i in range(m, n+1):
            a, b, c = [int(x) for x in list(str(i))]  # 用这种，这就是python的强大之处
            # a = i//100
            # b = i//10%10
            # c= i%10
            if a*a*a + b*b*b + c*c*c == i:
                flag = 0
                print(f'{i}={a}*{a}*{a}+{b}*{b}*{b}+{c}*{c}*{c}')
        if flag:
            print('none')
except EOFError:
    pass