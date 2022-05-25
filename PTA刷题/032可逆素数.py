# 7-32 可逆素数
# 作者 熊超
# 单位 浙江理工大学
# 输入两个正整数m和n，且m<n,求[m,n]之间的可逆素数列表。可逆素数：素数的各位数字顺序颠倒后得到的数仍是素数
#
# 输入格式:
# 分行输入m和n
#
# 输出格式:
# 输出可逆素数列表
#
# 输入样例1:
# 50
# 100
# 输出样例1:
# [71, 73, 79, 97]
# 输入样例2:
# 200
# 300
# 输出样例1:
# no exit
def is_sushu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


m = int(input())
n = int(input())
su_list = []
nisu_list = []
for i in range(m, n+1):
    if is_sushu(i):
        su_list.append(i)
for item in su_list:
    ni_item = int(str(item)[::-1])  # 逆序
    if is_sushu(ni_item):
        nisu_list.append(item)
if len(nisu_list) == 0:
    print('no exit')
else:
    print(nisu_list)



