# 某学校教职工人数不足n人，在操场排队，7个一排剩5人，5个一排剩3人，3个一排剩2人；请问该校人数有多少种可能？最多可能有几人？
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数n（1≤n≤10000）。
#
# 输出格式:
# 对于每组测试，输出一行，包含2个以一个空格间隔的整数，分别表示该校教职工人数的可能种数和最多可能的人数。
#
# 输入样例:
# 1000
# 输出样例:
# 9 908
try:
    while True:
        n = int(input())
        lst = []
        for i in range(n):
            if i % 7 == 5 and i % 5 == 3 and i % 3 == 2:
                lst.append(i)
        print(len(lst), max(lst))
except EOFError:
    pass