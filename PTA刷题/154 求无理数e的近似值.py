# 无理数e=1+1/1!+1/2!+1/3!+...
# 要求读入一个精度值，当累加项小于该值时，停止累加，最后输出累加和结果。
#
# 输入格式:
# 输入在一行中给出一个精度值，例如0.0001。
#
# 输出格式:
# 对每一组输入，在一行中输出e的值，结果保留10位小数。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 1e-8
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 2.7182818262
def jiecheng(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

e = eval(input())
sum = 1
count = 1
a = 1
b = 1
while True:
    if a / b < e:
        break
    sum += a/b
    count += 1
    b = jiecheng(count)
print(f'{sum:.10f}')