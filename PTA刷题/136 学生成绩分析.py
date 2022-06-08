# 输入考试的成绩（可以有小数），求出各分数与平均分的差值绝对值（保留一位小数）,输出按差值绝对值从小到大排列的（分数，差值绝对值）列表。
#
# 输入格式:
# 第一行输入同学们的考试成绩，以空格隔开。
#
# 输出格式:
# 输出排好序的（分数，差值绝对值）列表。
#
# 输入样例:
# 66 78 95 63 85 94 99
# 输出样例:
# [(85, 2.1), (78, 4.9), (94, 11.1), (95, 12.1), (99, 16.1), (66, 16.9), (63, 19.9)]
import math

score_list = list(map(str, input().split()))
score_list = [eval(x) for x in score_list]
lst = []
aver = sum(score_list) / len(score_list)
for i in score_list:
    my_triple = (i, round(math.fabs(aver - i), 1))
    lst.append(my_triple)
lst = sorted(lst, key=lambda x: x[1])
print(lst)
