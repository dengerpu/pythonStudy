class Student(object):
    def __init__(self, name , age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def show(self):
        print(self.name, self.age, self.gender, self.score)

if __name__ == '__main__':
    print('请输入三位学员的信息，（姓名#年龄#性别#成绩）')
    lst = []
    for i in range(3):
        s = input(f'请输入第{i+1}个学生的信息和成绩：')
        s_list = s.split('#')
        stu = Student(s_list[0], s_list[1], s_list[2], s_list[3])
        lst.append(stu)
    for item in lst:
        item.show()