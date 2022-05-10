import os


def create_files():
    '''
    批量创建文件
    '''
    for i in range (1, 11):
        file_name = 'text/file_'+str(i)+'.txt'
        # os.mkdir(file_name)
        f = open(file_name, 'w')
        f.close()


def create_files1():
    os.chdir('text')
    for i in range(11, 21):
        file_name = 'file_'+str(i)+'.txt'
        f = open(file_name, 'w')
        f.close()
    os.chdir('../')  # 重新返回上一级目录


# create_files()
# create_files1()

def modify_filename():
    '''
    批量修改文件名
    '''
    os.chdir('text')
    buf_list = os.listdir()  # 获取所有的文件目录
    for file in buf_list:
        new_file = 'python批量修改_'+file
        os.rename(file, new_file)
    os.chdir('../')


def modify_filename1():
    os.chdir('text')
    buf_list = os.listdir()
    for file in buf_list:
        num = len('python批量修改_')
        new_file = file[num:]
        os.rename(file, new_file)
    os.chdir('../')


# modify_filename()
modify_filename1()

