# 输入a,b班的名单，并进行如下统计。
#
# 输入格式:
# 第1行:：a班名单，一串字符串，每个字符代表一个学生，1个或多个空格分隔，可能有重复字符。数字代表男生，字母代表女生。
#
# 第2行:：b班名单，一串字符串，每个字符代表一个学生，1个或多个空格分隔，可能有重复学生。数字代表男生，字母代表女生。
#
# 第3行:：参加数学竞赛的学生，一串字符串，每个学生名称以1个或多个空格分隔。
#
# 第4行：参加计算机竞赛的学生，一串字符串，每个学生名称以1个或多个空格分隔。
#
# 输出格式:
# 注意：输出人员名单的时候需调用sorted函数，如集合为x，则print(sorted(x)) 。
#
# 输出两个班级的所有人员名单和数量。
# 输出两个班级中既参加数学，也参加计算机竞赛的名单和数量。
# 输出两个班级中参加比赛的女名单和数量。
# 输出两个班级中只参加数学竞赛的名单。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 1 2 3  4 a s d f
# 6 7 8 9 6 5 z x c
# 2 3 a s 8 9 z
# 1 3 4 s d 5 9 x z
# 输出样例:
# 在这里给出相应的输出。例如：
#
# Total: ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'c', 'd', 'f', 's', 'x', 'z'], num: 16
# Math and jsj: ['3', '9', 's', 'z'], num: 4
# FeMale in race: ['a', 'd', 's', 'x', 'z'], num: 5
# Only Math: ['2', '8', 'a']

class_a = set(input().split())
class_b = set(input().split())
math_contest = set(input().split())
computer_contest = set(input().split())

class_all = class_a | class_b
race_all = math_contest & computer_contest
female = []
for i in class_all:
    if not(48 <= ord(i) <= 57):
        female.append(i)
race_female = set(female) & (math_contest | computer_contest)
race_math = math_contest - race_all
print(f'Total: {sorted(class_all)}, num: {len(class_all)}')
print(f'Math and jsj: {sorted(race_all)}, num: {len(race_all)}')
print(f'FeMale in race: {sorted(race_female)}, num: {len(race_female)}')
print(f'Only Math: {sorted(race_math)}')
