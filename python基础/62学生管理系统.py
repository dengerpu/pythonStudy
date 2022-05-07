# 定义学生列表，保存所有学生信息
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


def insert_student():
    """
    添加学生信息
    :return:
    """
    # 1. 通过 input 函数获取学生的信息, 姓名, 年龄, 性别
    name = input('请输入姓名：')
    sex = input('请输入性别：')
    age = input('请输入年龄：')
    # [{}, {}, {}]  判断的是字典中的 value 是否存在
    for stu in stu_list:
        if stu['name'] == name:
            print('----------学生信息存在---------')
            return  # 结束函数的执行
    # 2. 将学生信息转换为字典进行保存
    stu_dict = {'name': name, 'age': age, 'sex': sex}
    # 3. 将这个学生字典添加的列表中
    stu_list.append(stu_dict)
    print('==============学生信息添加成功====================')


def delete_stu():
    """
    显示单个学生信息
    """
    name = input('请输入要删除的学生姓名:')
    for stu in stu_list:
            if stu['name'] == name:
               stu_list.remove(stu)
               break
    else:
        print('***********该学生信息不存在,无法删除**************')


def modify_stu():
    """
    显示单个学生信息
    """
    name = input('请输入要修改的姓名:')
    for stu in stu_list:
            if stu['name'] == name:
                age = input('请输入新的年龄：')
                stu['age'] = age
                print('修改成功')
                break
    else:
        print('----------学生信息不存在---------')


def show_one_stu():
    """
    显示单个学生信息
    """
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


def main():
    '''
    主函数
    '''
    while True:
        show_menu()
        option = input('请输入操作：')
        if option == '1':
            insert_student()
        elif option == '2':
            delete_stu()
        elif option == '3':
            modify_stu()
        elif option == '4':
            show_one_stu()
        elif option == '5':
            show_all_stu()
        elif option == '6':
            print('6. 退出系统')
            break
        else:
            print('输入有误，请重新输入')
            continue

        input('...... 回车键继续操作.......')


main()