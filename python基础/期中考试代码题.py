# 24**.元素分类有如下值集合
# [11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key对应的值中，将小于66的值保存至第二个key对应的值中*★
my_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
my_dict = {'key1': [], 'key2': []}
for i in my_list:
    if i > 66:
        my_dict['key1'].append(i)
    else:
        my_dict['key2'].append(i)
print(my_dict)

# 25**.统计字符串中字符出现的次数，如果是空格，不输出
# 如: "hello world"字符串统计的结果为:{'l: 3, 'h':1, 'w': 1, 'd': 1, 'o': 2, 'r': 1, 'e': 1}
my_str = "hello world"
my_dict = {}
for i in my_str:
    if i == ' ':
        continue
    my_dict[i] = my_str.count(i)

print(my_dict)



