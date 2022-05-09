#  列表排序，列表中的数据类型要保持一致
my_list = [1, 3, 5, 4, 2, 1, 9, 6]
my_list.sort()
print(my_list)

list1 = [{'name': 'd', 'age': 16},
        {'name': 'a', 'age': 16},
        {'name': 'a', 'age': 10},
        {'name': 'b', 'age': 10},
        {'name': 'c', 'age': 19}
         ]
# list1.sort()  # 程序报错
# 匿名函数的形参是列表中的每一个数据
list1.sort(key=lambda x: x['name'])
print(list1)
print('='*30)
list1.sort(key=lambda x: x['age'])
print(list1)

list2 = ['aghdd', 'bc', 'ghlj', 'def']
list2.sort(key=len)
print(list2)
list2.sort(key=lambda x:len(x),reverse=True)
print(list2)

# sort(key= lambda 形参：（排列规则1，排列规则2....）)
# 当第一个规则相同，会按照第二个规则排
list1.sort(key=lambda x: (x['name'], x['age']))
print(list1)
list1.sort(key=lambda x: (x['age'], x['name']))
print(list1)