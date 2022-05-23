"""
读入两个整数a和b，输出绝对值a和绝对值b的各对应位乘积之和，如a=1234，b=608，则输出值为：“1×0+2×6+3×0+4×8“的值，即44。
输入格式:
在一行中输入两个数
输出格式:
在一行中输出对应位乘积之和
输入样例:
在这里给出一组输入。例如：
1234 608
输出样例:
在这里给出相应的输出。例如：
44
"""

value = input()
a, b = value.split()
a = a.replace('-', '', 1)  # 相当于取绝对值
b = b.replace('-', '', 1)
length = len(a) if len(a) > len(b) else len(b)   # 求出两个数长度最大值
if len(a) != length:   # 前面补0，位数补成一样
    a = '0'*(length-len(a))+a
if len(b) != length:
    b = '0'*(length-len(b))+b
a_list = list(a)  # 转化成字符数组
b_list = list(b)
# for index, item in enumerate(a_list):  # 字符数组转换成整形数组,可以用下面的列表推导式更简单
#     a_list[index] = int(item)
# for index, item in enumerate(b_list):
#     b_list[index] = int(item)
a_list = [int(x) for x in a_list]
b_list = [int(x) for x in b_list]
result = 0
for a, b in zip(a_list, b_list):
    result += a*b
print(result)



