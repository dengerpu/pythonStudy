import os
# 使用文件操作，向`movie.txt`文件中写入一下内容：
# 功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥

f = open('move.txt', 'w', encoding='utf-8')
f.write('功夫，周星驰\n一出好戏，黄渤\n我不是药神，徐峥')
f.write("""功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥""")
f.close()


# 将第一题创建好的文件打开，并读取内容， 要求如下：
# * 一次全部读取
#  * 每次读取一行
f = open('move.txt', 'r', encoding='utf-8')
# buf = f.read()  # 一次全部读取
buf_list = f.readlines()  # ['功夫，周星驰\n', '一出好戏，黄渤\n', '我不是药神，徐峥功夫，周星驰\n', '一出好戏，黄渤\n', '我不是药神，徐峥']
buf = [i.strip() for i in buf_list]
print(buf)
f.close()

print('='*20)

f = open('move.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()  # 一次读取一行
    if buf:
        print(buf, end='')
    else:
        break
f.close()


# - 使用os模块创建一个名为“黑马”的文件夹
# - 获取黑马文件夹当前所在目录
# - 获取当前的目录列表
# - 改变文件的操作路径
# - 将黑马文件夹删除
print()
# os.mkdir('黑马')
print(os.getcwd())
print(os.listdir('./'))
print(os.listdir())
# os.chdir('../')
# print(os.getcwd())
# os.rmdir('黑马')

# 编写一段代码以完成两份文件之间的相互备份
# * 提示用户输入文件名。例：gailun.txt
# - 创建以用户输入的名字的文件
# - 打开文件写入如下信息
#   功夫，周星驰
#  一出好戏，黄渤
#  我不是药神，徐峥
# - 将输入的数据输出到终端上
# - 在文件夹中创建gailun副本.txt文件
# - 将gailun.txt文件中的数据写入gailun副本.txt文件中
# - 打开文件，查看文件中内容
# name = input('请输入要创建的文件名字')
# f = open(name, 'w', encoding='utf-8')
# f.write("""功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥""")
# f.close()
# f = open(name, 'r', encoding='utf-8')
# buf = f.read()
# print(buf)
# f.close()
# index = name.rfind('.')
# if index:
#      new_filename = name[:index]+'副本'+name[index:]
# f = open(new_filename, 'w', encoding='utf-8')
# f.write(buf)
# f.close()


# - 创建一个新项目中新创建一个名字py文件夹
# - 进入py文件夹中创建5个文件，文件名分别为python基础班-1.txt，python基础班-2.txt，python基础班-3.txt，python基础班-4.txt，python基础班-5.txt
# - 然后将py文件夹中的所有文件都改名为[黑马]python基础班-1.txt，[黑马]python基础班-2.txt，[黑马]python基础班-3.txt，[黑马]python基础班-4.txt，[黑马]python基础班-5.txt
# os.mkdir('py')
os.chdir('py')
# for i in range(1, 6):
#     name = 'python基础班-'+str(i)+'.txt'
#     # os.mkdir(name)  # 这样创建的是文件夹
#     f = open(name, 'w')
#     f.close()
# file_list = os.listdir()
# print(file_list)
# for file in file_list:
#     new_name = '[黑马]'+file
#     os.rename(file,new_name)
for i in range(6,11):
    f = open("python基础班-%d.txt" % i,'w')
    f.close()
