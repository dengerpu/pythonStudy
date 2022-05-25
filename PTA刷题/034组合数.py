# 输入两个正整数n、m，要求输出组合数C(n,m)。
# 例如，当n=5、m=3时，组合数C(5,3)=(5×4×3)/(3×2×1)=10。
# 组合数可用以下公式计算：
#
# Cn m = n!/(m!*(n-m)!)
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入两个整数n，m（0 < m ≤ n ≤ 20）。
#
# 输出格式:
# 对于每组测试，输出组合数。
#
# 输入样例:
# 5 3
# 20 12
# 输出样例:
# 10
# 125970
def Factorial(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i += 1
    return result

lst = []
while True:
    value = input()
    if value.strip() == '':
        break
    n, m = list(map(int, value.split()))
    result = Factorial(n)/(Factorial(m)*Factorial(n-m))
    lst.append(int(result))
for i in lst:
    print(i)