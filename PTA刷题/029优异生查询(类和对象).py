# 题目： 编程实现查找优异生的功能——用户输入多个学生的成绩，输出总分最高的学生姓名和各科成绩
# 要求： 设计一个学生类（Student），包括
#
# 1）属性：姓名(name)，数学成绩(mscore)，语文成绩(cscore)，英语成绩(escore)；
#
# 2）方法：
#
# 构造方法，来构造每个具体的学生对象
# 计算总成绩方法getSum(self)，返回三个成绩的和
# 获得优异生姓名,数学成绩,语文成绩,英语成绩的方法getBest(self)，返回4个结果内容（优异生姓名,数学成绩,语文成绩,英语成绩）
# 输入格式:
# 通过4行输入：
#
# 第一行输入多个学生姓名，以空格分隔
#
# 第二行输入多个数学成绩，以空格分隔
#
# 第三行输入多个语文成绩，以空格分隔
#
# 第四行输入多个英语成绩，以空格分隔
#
# 注意：学生姓名个数要和成绩个数保持一致
#
# 输出格式:
# 在一行中，输出总分最高的学生及其各科科目成绩，以空格分隔。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# Jack Tom Jim
# 95 84 32
# 90 75 45
# 85 90 67
# 输出样例:
# 在这里给出相应的输出。例如：
#
# Jack 95 90 85
class Student(object):
    def __init__(self, name, mscore, cscore, escore):
        self.name = name
        self.mscore = mscore
        self.cscore = cscore
        self.escore = escore

    def getSum(self):
        self.count = float(self.mscore) + float(self.cscore) + float(self.escore)
        return  self.count

    def getBest(self):
        print(self.name, self.mscore, self.cscore, self.escore)

lst = []
class_list = []
for i in range(4):
    item_list = input().split()
    lst.append(item_list)
for i in range(len(lst[0])):
    stu_list = []
    for j in range(4):
        stu_list.append(lst[j][i])
    stu = Student(stu_list[0], stu_list[1], stu_list[2], stu_list[3])
    class_list.append(stu)
max_stu = class_list[0]
for stu1 in class_list:
    if stu1.getSum() > max_stu.getSum():
        max_stu = stu1
max_stu.getBest()



