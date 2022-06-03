# 同一行中输入m和n二个正整数，n作为seed种子，产生一个4位的随机数验证码，该随机数作为下一个seed种子，再产生一个4位随机数验证码......直至产生m个随机数验证码。产生的m个随机数验证码按样例输出。
#
# m,n=input().split() #同一行中输入m,n
#
# randint(1000,9999) #生成一个【1000，9999】之间的整数
#
# 输入格式:
# 同一行中输入m和n。二数之间用空隔隔开。
#
# 输出格式:
# 分m行输出。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 2  8
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 4714
# 1142
# import numpy as np
# # 随机种子生成器，使下一次生成的随机数为由种子数决定的“特定”的随机数，如果seed中参数为空，则生成的随机数“完全”随机
# m, n = map(int, input().split())
# for i in range(m):
#     np.random.seed(n)
#     n = np.random.randint(1000, 9999)
#     print(n)
import random

m, n = map(int, input().split())
for i in range(m):
    random.seed(n)
    n = random.randint(1000, 9999)
    print(n)