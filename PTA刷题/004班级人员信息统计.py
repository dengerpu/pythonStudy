# 输入a,b班的名单，并进行如下统计。
#
# 输入格式:
# 第1行:：a班名单，一串字符串，每个字符代表一个学生，无空格，可能有重复字符。
# 第2行:：b班名单，一串字符串，每个学生名称以1个或多个空格分隔，可能有重复学生。
# 第3行:：参加acm竞赛的学生，一串字符串，每个学生名称以1个或多个空格分隔。
# 第4行：参加英语竞赛的学生，一串字符串，每个学生名称以1个或多个空格分隔。
# 第5行：转学的人(只有1个人)。
#
# 输出格式
# 特别注意：输出人员名单的时候需调用sorted函数，如集合为x，则print(sorted(x))
# 输出两个班级的所有人员数量
# 输出两个班级中既没有参加ACM，也没有参加English的名单和数量
# 输出所有参加竞赛的人员的名单和数量
# 输出既参加了ACM，又参加了英语竞赛的所有人员及数量
# 输出参加了ACM，未参加英语竞赛的所有人员名单
# 输出参加英语竞赛，未参加ACM的所有人员名单
# 输出参加只参加ACM或只参加英语竞赛的人员名单
# 最后一行：一个同学要转学，首先需要判断该学生在哪个班级，然后更新该班级名单，并输出。如果没有在任何一班级，什么也不做。
#
# 输入样例:
# abcdefghijab
# 1   2 3 4 5 6 7 8 9  10
# 1 2 3 a b c
# 1 5 10 a d e f
# a
# 输出样例:
# Total: 20
# Not in race: ['4', '6', '7', '8', '9', 'g', 'h', 'i', 'j'], num: 9
# All racers: ['1', '10', '2', '3', '5', 'a', 'b', 'c', 'd', 'e', 'f'], num: 11
# ACM + English: ['1', 'a'], num: 2
# Only ACM: ['2', '3', 'b', 'c']
# Only English: ['10', '5', 'd', 'e', 'f']
# ACM Or English: ['10', '2', '3', '5', 'b', 'c', 'd', 'e', 'f']
# ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

class_list1 = []  # 记录一班学生信息
class_list2 = []  # 记录二班学生信息
acm_list = []  # 参加acm竞赛的学生
english_list = []  # 参加英语竞赛的学生
norace_list = []  # 没有参加竞赛的学生
race_list = []  # 所有参赛
race_all_list =[]   # 两个都参加
race_englist_list = []  # 只参加英语
race_acm_list = []      # 只参加acm
race_one_list = []      # 只参加一个

class1 = input()  # 输入一班的学生信息
class2 = input()  # 输入二班的学生信息
acm = input()  # 输入参加acm竞赛的同学
english = input()  # 输入参加英语竞赛的同学
student = input()  # 转学的学生
for stu in class1:
    if stu not in class_list1:
        class_list1.append(stu)
for stu in class2.split():
    if stu not in class_list2:
        class_list2.append(stu)
for stu in acm.split():
    acm_list.append(stu)
for stu in english.split():
    english_list.append(stu)
total_student = len(class_list1)+len(class_list2)  # 两个班所有的人员数量
for stu in class_list1:
    if (stu not in acm_list) and ( stu not in english_list) :
        norace_list.append(stu)
    if (stu in acm_list) or (stu in english_list):
        race_list.append(stu)
    if (stu in acm_list) and (stu in english_list):
        race_all_list.append(stu)
    if (stu in acm_list) and (stu not in english_list):
        race_acm_list.append(stu)
    if (stu not in acm_list) and (stu in english_list):
        race_englist_list.append(stu)
    if (stu in acm_list) or (stu in english_list):
        if not ((stu in acm_list) and (stu in english_list)):
            race_one_list.append(stu)
for stu in class_list2:
    if (stu not in acm_list) and ( stu not in english_list) :
        norace_list.append(stu)
    if (stu in acm_list) or (stu in english_list):
        race_list.append(stu)
    if (stu in acm_list) and (stu in english_list):
        race_all_list.append(stu)
    if (stu in acm_list) and (stu not in english_list):
        race_acm_list.append(stu)
    if (stu not in acm_list) and (stu in english_list):
        race_englist_list.append(stu)
    if (stu in acm_list) or (stu in english_list):
        if not((stu in acm_list) and (stu in english_list)):
            race_one_list.append(stu)
print(f'Total: {total_student}')
print(f'Not in race: {sorted(norace_list)}, num: {len(norace_list)}')
print(f'All racers: {sorted(race_list)}, num: {len(race_list)}')
print(f'ACM + English: {sorted(race_all_list)}, num: {len(race_all_list)}')
print(f'Only ACM: {sorted(race_acm_list)}')
print(f'Only English: {sorted(race_englist_list)}')
print(f'ACM Or English: {sorted(race_one_list)}')
if student in class_list1:
    class_list1.remove(student)
    print(class_list1)
elif student in class_list2:
    class_list2.remove(student)
    print(class_list2)
