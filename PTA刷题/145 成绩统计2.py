# 输入一个正整数n(n>=1)，然后输入n行数据，表示的是某班各位同学的各科成绩（每位同学的考试科目都相同），请统计出各门课程的平均分(保留2位小数)。
#
# 输入格式:
# 先一个正整数n(n>=1),然后输入n行数据
#
# 输出格式:
# 输出各门课程的平均分
#
# 输入样例:
# 2
# {'语文':95,'数学':82,'英语':75}
# {'语文':98,'数学':72,'英语':85}
# 输出样例:
# 语文:96.50
# 数学:77.00
# 英语:80.00
n = int(input())
my_dict = {}
for i in range(n):
    if i == 0:
        my_dict = eval(input())
    else:
        dict1 = eval(input())
        for key in dict1:
            if key in my_dict:
                my_dict[key] += dict1[key]
for key in my_dict:
    my_dict[key] = my_dict[key] / n
for key, value in my_dict.items():
    print(f'{key}:{value:.2f}')