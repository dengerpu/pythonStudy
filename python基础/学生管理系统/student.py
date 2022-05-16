class Student(object):
    def __init__(self, id, name, age, sex):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'{self.id},{self.name},{self.age},{self.sex}'


if __name__ == '__main__':
    stu = Student(1, 'admin', 15, '男')
    print(stu)