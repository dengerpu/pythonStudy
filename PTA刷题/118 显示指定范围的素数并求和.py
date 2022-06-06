# 本题要求显示给定整数M和N区间内素数并对它们求和。
#
# 输入格式:
# 在一行输入两个正整数M和N（1≤M≤N≤1000）。
#
# 输出格式:
# 显示指定范围的素数，素数间空一格，每五个换一行。
# 单独一行输出素数的个数及素数的和。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 4 30
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 5 7 11 13 17
# 19 23 29
# amount=8 sum=124
def print_list(lst):
    for i in range(len(lst)):
        if (i+1) % 5 == 0:
            print(lst[i], end=' \n')
        else:
            print(lst[i],end=' ')

m, n = map(int, input().split())
lst = []
for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print_list(lst)
if (len(lst)) % 5 != 0:
    print()
print(f'amount={len(lst)} sum={sum(lst)}', end='')
