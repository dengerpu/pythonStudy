# 本题目要求读入2个不超过100的非0正整数A和B，然后输出(0,A]中所有能被B整除的数。
#
# 输入格式:
# 输入在一行中给出2个不超过100的非零正整数A和B。
#
# 输出格式:
# 对每一组输入，在一行中输出(0,A]中所有能被B整除的数，数字之间用空格分隔，最后一个数字后面没有空格。
# 如果没有这样的数，输出“None.”
#
# 输入样例1:
# 37 5
# 输出样例1:
# 5 10 15 20 25 30 35
# 输入样例2:
# 37 40
# 输出样例2:
# None.
a, b = map(int, input().split())
lst = []
flag = 1
if a >= b:
    for i in range(1, a+1):
        if i % b == 0:
            lst.append(i)
if len(lst) == 0:
   print('None.')
else:
    for i in range(len(lst)-1):
        print(lst[i], end=' ')
    print(lst[-1])