# 小明在帮老师处理数据，这些数据的第一行是n，代表有n行整数成绩需要统计。
# 接着连续输入n个成绩，如果中途输入错误（非整数）提示'Error! Reinput',
# 并输出错误的数据。然后重新输入，直到输入n个正确的成绩才退出。如果整个
# 输入过程中没有错误数据，提示'All OK'。最后输出所有学生的平均值，保留两
# 位小
# 数。
#
# 注：该程序可以适当处理小错误，比如对于有些数据如果左右包含空格，先去掉
# 空格再行处理。
#
# 输入格式:
# 第一行为n，代表接下来要输入的正确行数。
# 然后输入成绩，输入错误则提示重输，直到输入n行正确的数据为止。
#
# 输出格式:
# 如果输入过程中无异常，需输出All OK。
#
# 输入样例1:
# 3
# 1
#   2
#     3
# 输出样例1:
# All OK
# avg grade = 2.00
# 输入样例2:
# 3
# 1
# #
# b
# 2
# 3
# 输出样例2:
# Error for data #! Reinput
# Error for data b! Reinput
# avg grade = 2.00
n = int(input())
count = 0
result = 0
flag = 0  # 用于记录最后是否打印ALL ok
while count < n:
    try:
        value = input().strip()
        num = int(value)
        result += num
        count += 1
        flag += 1
    except Exception:
        flag += 1
        print(f'Error for data {value}! Reinput')
if(flag == n):
    print('All OK')
print(f'avg grade = {result/count:.2f}')
