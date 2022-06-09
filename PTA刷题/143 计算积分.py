# 女排世界杯参赛队伍为12只，比赛采取单循环方式，五局三胜制，比赛以3-0或者3-1取胜的球队积3分、负队积0分，以3-2取胜的球队积2分、负队积1分；输入n，及n支球队的比分情况，编写程序计算各队的积分，并从高到低排序输出。
#
# 输入格式:
# 先输入一行n表示有n(n>=2)支球队
# 再输入n行数据表示各队的比分情况，球队名称(不重复)和比分之间用:(英文)分隔，比分用-分隔，如3-0表示该球队获胜，0-3表示该球队输球，每场比分之间用逗号分隔。
#
# 输出格式:
# 按积分从高到低排序，输出球队名称及积分
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 2
# 中国队:3-0,3-1,3-2,3-1,3-0
# 美国队:3-1,3-1,0-3,1-3,2-3
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 中国队 : 14
# 美国队 : 7
n = int(input())
my_dict = {}
for i in range(n):
    country, score = input().split(":")
    score_list = score.split(',')
    my_dict[country] = 0
    for item in score_list:
        a, b = list(map(int ,item.split('-')))
        if a == 3 and (b == 0 or b == 1):
            my_dict[country] += 3
        if a == 3 and b == 2:
            my_dict[country] += 2
        if a == 2 and b == 3:
            my_dict[country] += 1
count = 0
my_dict_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
for item in my_dict_list:
    count += 1
    if count != len(my_dict_list):
        print(f'{item[0]} : {item[1]}')
    else:
        print(f'{item[0]} : {item[1]}', end='')
