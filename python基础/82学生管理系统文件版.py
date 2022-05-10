# 定义一个列表，存储学生信息
stu_list = []

def show_menu():
    '''
     菜单
     :return:
     '''
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')


def add_student():
    name = input('请输入姓名:')
    age = input('请输入年龄：')
    sex = input('请输入性别：')
    for stu in stu_list:
        if stu['name'] == name:
            print('...... 学生信息已存在.......')
            break
    my_dict = {'name': name, 'age': age, 'sex': sex}
    stu_list.append(my_dict)
    save_info()
    print('...... 添加成功.......')


def delete_student():
    name = input('请输入要删除的学生：')
    for stu in stu_list:
        if stu['name'] == name:
            stu_list.remove(stu)
            print('...... 删除成功.......')
            save_info()
            break
    else:
        print('...... 不存在学生信息.......')



def modify_student():
    name = input('请输入要修改的学生信息：')
    for stu in stu_list:
        if stu['name'] == name:
            age = input('请输入要修改的年龄：')
            stu['age'] = age
            print('...... 修改成功.......')
            save_info()
            break
    else:
        print('...... 不存在学生信息.......')


def find_student():
    name = input('请输入要查找的姓名:')
    for stu in stu_list:
        if stu['name'] == name:
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["sex"]}')
            break
    else:
        print('----------学生信息不存在---------')


def show_all_stu():
    """
    显示所有学生信息
    """
    if len(stu_list)>0:
        for stu in stu_list:
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["sex"]}')
    else:
        print('----------学生信息存在---------')


def save_info():
    f = open('student.txt', 'w', encoding='utf-8')
    f.write(str(stu_list))
    f.close()


def read_info():
    f = open('student.txt', 'r', encoding='utf-8')
    buf = f.read()
    global stu_list
    stu_list = eval(buf)
    # print(len(stu_list))
    f.close()

def main():
    read_info()
    while True:
        show_menu()
        option = input('请输入操作：')
        if option == '1':
            add_student()
        elif option == '2':
            delete_student()
        elif option == '3':
            modify_student()
        elif option == '4':
            find_student()
        elif option == '5':
            show_all_stu()
        elif option == '6':
            print('退出系统')
            break
        else:
            print('输入有误，请重新输入')
            continue
        input('...... 回车键继续操作.......')


# save_info()
main()
# read_info()

