# 同一行中输入m、n和k，n作为seed种子，产生一个k位的随机数验证码，该随机数作为下一个seed种子，再产生一个k位随机数验证码......直至产生m个随机数验证码。产生的m个随机数验证码按样例输出。
#
# m,n,k=input().split() #同一行中输入m,n,k
#
# randint(1000,9999) #生成一个【1000，9999】之间的整数
#
# 输入格式:
# 同一行中输入m、n和k。各数之间用空隔隔开。
#
# 输出格式:
# 分m行输出。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 3 4 5
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 40939
# 33119
# 26241
import math
import random

m, n, k = map(int,input().split())
for i in range(m):
    random.seed(n)
    n = random.randint(int(math.pow(10, k-1)), int(math.pow(10, k))-1)
    print(n)