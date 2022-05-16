import student
class student_manger_system(object):
    def __init__(self):
        self.__stu_dicts = {}

    @staticmethod
    def __show_menu():
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 修改学生信息')
        print('4. 查询单个学生信息')
        print('5. 查询所有的学生信息')
        print('6. 退出系统')

    # 添加学生
    def __insert_student(self):
        id = input('请输入学生id：')
        # 代码优化, 判断学生信息是否存在, 学号是否存在. 判断字典的key是否存在
        if id in self.__stu_dicts:
            print('学生信息已经存在, 不需要再次添加.........')
            return
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')
        sex = input('请输入学生性别：')
        # 2. 使用学生信息,创建学生对象  学生类(参数)
        stu = student.Student(id, name, age, sex)
        # 3. 将学生对象添加的字典中 字典['key'] = 数据值
        self.__stu_dicts[id] = stu
        print('添加成功....')

    # 删除学生
    def __remove_student(self):
        id = input('请输入要删除的学生学号：')
        if id in self.__stu_dicts:
            del self.__stu_dicts[id]
            print('删除成功....')
        else:
            print('不存在该学生信息...')

    # 修改学生
    def __modify_student(self):
        id = input('请输入要修改的学生学号：')
        if id in self.__stu_dicts:
            stu = self.__stu_dicts[id]
            stu.age = input('请输入新的年龄：')
            print('信息修改成功...')
        else:
            print('不存在该学生信息...')

    # 打印所有学生
    def __show_all_info(self):
        if len(self.__stu_dicts) > 0:
            for stu in self.__stu_dicts:
                print(self.__stu_dicts[stu])
        else:
            print('还没有学生信息....')

    # 查找单个学生
    def __search_student(self):
        id = input('请输入要查找的学生学号：')
        if id in self.__stu_dicts:
            stu = self.__stu_dicts[id]
            print(stu)
        else:
            print('不存在该学生信息...')

    def __save(self):
        f = open('student.txt', 'w', encoding='utf-8')
        for stu in self.__stu_dicts.values():
            f.write(str(stu) + '\n')
        f.close()

    def __load_info(self):
        try:
            f = open('student.txt', 'r', encoding='utf-8')
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()  # 去掉\n
                info_list = buf.split(',') # 列表
                stu = student.Student(*info_list)
                self.__stu_dicts[info_list[0]] = stu
            f.close()
        except Exception:
            pass

    def start(self):
        self.__load_info()
        while True:
            self.__show_menu()
            opt= input('请输入要选择的操作：')
            if opt == '1':
                # print('1. 添加学生')
                self.__insert_student()
            elif opt == '2':
                # print('2. 删除学生')
                self.__remove_student()
            elif opt == '3':
                # print('3. 修改学生信息')
                self.__modify_student()
            elif opt == '4':
                # print('4. 查询单个学生信息')
                self.__search_student()
            elif opt == '5':
                # print('5. 查询所有的学生信息')
                self.__show_all_info()
            elif opt == '6':
                self.__save()
                print('欢迎下次使用本系统......')
                break
            else:
                print('输入有误,请再次输入')
                continue

            input('...... 回车键继续操作.......')
