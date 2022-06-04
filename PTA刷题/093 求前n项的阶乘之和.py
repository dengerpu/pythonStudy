# 从键盘输入一个正整数n,求前n项的阶乘之和，1!+2!+3!+...+n!的和
#
# #####输入样例:
#
# 在这里给出一组输入。例如：
#
# 3
# 输出样例:
# 9
n = int(input())
sum = 0
for i in range(1,n+1):
    result = 1
    for j in range(1,i+1):
        result *= j
    sum += result
print(sum)
