# 本题目要求读入1个整数A，然后输出该数字每位数的累加和，要求使用列表推导式实现。
#
# 输入格式:
# 输入在一行中给出1个任意长度的整数（可正可负）。
#
# 输出格式:
# 对每一组输入，在一行中输出其绝对值每位数字累加和。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# 12006
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# 9
# 输入样例2:
# 在这里给出一组输入。例如：
#
# -12006
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# 9
n = input().replace('-', '')
lst = [int(x) for x in n]
print(sum(lst))
