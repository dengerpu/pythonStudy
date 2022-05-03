import random

# 为8个老师随机分配3个办公室

schools = [[], [], []]  #定义学校列表

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for teacher in teachers:
    num = random.randint(0,2) #生成0-2的随机数 包括0-2
    schools[num].append(teacher)

print(schools)
for office in  schools:
    print(f'该办公室有{len(office)}个老师，分别是：')
    for teacher in office:
        print(teacher,end=' ')
    print()
