# 古希腊数学家毕达哥拉斯在自然数研究中发现，220的所有真约数（即不是自身的约数）之和为：1+2+4+5+10+11+20+22+44+55+110＝284。而284的所有真约数为1、2、4、71、 142，加起来恰好为220。人们称这样的数对为亲和数。也就是说，若两个数中任何一个数都是另一个数的真约数之和，则它们就是亲和数。请判断输入的两个整数是否是亲和数。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入两个正整数a，b。
#
# 输出格式:
# 对于每组测试，若a，b是亲和数，是则输出“YES”，否则输出“NO”。引号不必输出。
#
# 输入样例:
# 220 284
# 输出样例:
# YES
def proton(n):
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    return lst

try:
    while True:
        a, b = map(int, input().split())
        listA = proton(a)
        listB = proton(b)
        if sum(listA) == b and sum(listB) == a:
            print('YES')
        else:
            print('NO')
except EOFError:
    pass
