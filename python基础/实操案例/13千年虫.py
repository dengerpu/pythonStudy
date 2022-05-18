my_list = [82, 88, 98, 86, 92, 00, 99]
print('原列表：', my_list)

for index,value in enumerate(my_list):
    if str(value) != '0':
        my_list[index] = int('19' + str(value))
    else:
        my_list[index] = int('200' + str(value))

print('修改后的列表：', my_list)
