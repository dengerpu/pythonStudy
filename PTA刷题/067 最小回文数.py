# 若一个数正向看和反向看等价，则称做回文数。例如：6，2552，12321均是回文数。
# 给出一个正整数n，求比n大的最小的回文数。（n和运算结果均不会超出int类型范围）
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入1个正整数n。
#
# 输出格式:
# 对于每组测试数据，输出比n大的最小回文数。
#
# 输入样例:
# 2
# 12
# 123456
# 输出样例:
# 22
# 124421
def symmetric(n):
    my_str = str(n)
    if my_str == my_str[::-1]:
        return True
    else:
        return False


t = int(input())
for i in range(t):
    n = input()
    end = int(n+n)  # 肯定不会超过这个范围，相当于字符串拼接。这个也肯定是回文字符串
    n = int(n)
    for i in range(n, end+1):
        if symmetric(i):
            print(i)
            break

