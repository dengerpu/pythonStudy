# 编写一个程序，从键盘读取k，计算e的近似值（保留10位小数）。
#
# 1023a.png
#
# 输入格式:
# >5的正整数k
#
# 输出格式:
# e的近似值（保留10位小数）
#
# 输入样例:
# 6
# 输出样例:
# 2.7180555556
def Factorial(n):
    result = 1
    if n == 0:
        return result
    for i in range(1, n+1):
        result *= i
    return result


k = int(input())
sum = 0
for i in range(k+1):
    sum += 1 / Factorial(i)
print('%.10f' % sum)