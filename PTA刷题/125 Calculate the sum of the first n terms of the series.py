# Calculate the sum of the first n terms of the series 1-2/3+3/5-4/7+5/9-6/11+...
#
# 输入格式:
# Enter a positive integer n.
#
# 输出格式:
# Output the value of the partial sum, retaining three decimal places.
#
# 输入样例:
# 5
# 输出样例:
# 0.917
n = int(input())
k = 1
sum = 0
for i in range(1,n+1):
    a = i
    b = 2*i-1
    result = k*a/b
    sum += result
    k = -k
print('%.3f' % sum)