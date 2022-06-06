# 输入n个学生的姓名及其3门功课成绩，要求按输入的逆序逐行输出每个学生的姓名、3门课成绩和平均成绩。若有学生平均成绩低于60分，则不输出该学生信息。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据首先输入一个正整数n(1<n<100)，表示学生人数；然后是n行信息，分别表示学生的姓名（长度不超过10且由英文字母构成的字符串）和3门课成绩（正整数）。
#
# 输出格式:
# 对于每组测试，输出所有满足要求的学生信息，每行一个学生信息：姓名、3门课成绩和平均成绩（保留2位小数）。每行的每两个数据之间留一个空格。
#
# 输入样例:
# 3
# zhangsan 80 75 65
# lisi 65 52 56
# wangwu 87 86 95
# 6
# zhangsan 80 75 65
# qisi 78 77 56
# wangwu 87 86 95
# zisi 78 77 56
# wangwu 88 86 95
# lisi 65 52 56
# 输出样例:
# wangwu 87 86 95 89.33
# zhangsan 80 75 65 73.33
# wangwu 88 86 95 89.67
# zisi 78 77 56 70.33
# wangwu 87 86 95 89.33
# qisi 78 77 56 70.33
# zhangsan 80 75 65 73.33
class Student(object):
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.aver = (x+y+z)/3

    def __str__(self):
        return f'{self.name} {self.x} {self.y} {self.z} {self.aver:.2f}'

try:
    while True:
        n = int(input())
        lst = []
        for i in range(n):
            name, x, y, z = input().split()
            student = Student(name, int(x), int(y), int(z))
            lst.append(student)
        for j in range(n):
            student = lst.pop()
            if student.aver >= 60:
                print(student)
except EOFError:
    pass