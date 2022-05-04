# 有一个列表，判断列表中的每一个元素是否以s或e结尾，
# 如果是，则将其放入一个新的列表中，最后输出这个新的列表
lists = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
new_list = []
for item in lists:
    if item[-1] == 's' or item[-1] == 'e':
        new_list.append(item)
print(new_list)
# 方法二
new_list1 = []
for item in lists:
    if item.endswith('s') or item.endswith('e'):
        new_list1.append(item)
print(new_list1)


# 给定一个列表，首先删除以s开头的元素，删除后，
# 修改第一个元素为"joke"，并且把最后一个元素复制一份，放在joke的后边
my_list = ["spring", "look", "strange", "curious", "black", "hope"]
for i in my_list:
    if i.startswith('s'):  # 后者i[0] == 's'
        my_list.remove(i)
my_list[0] = 'joke'
my_list.insert(1,my_list[-1])
print(my_list)

# 将下列两个列表合并，将合并后的列表去重，之后降序并输出
list1 = [11,  4, 45, 34, 51, 90]
list2 = [4, 16, 23, 51, 0]
my_list = list1  # 后者my_list = list1 + list2
my_list.extend(list2)
print(my_list)
my_list2 = []
for i in my_list:
    if i not in my_list2:
        my_list2.append(i)
my_list2.sort(reverse=True)
print(sorted(my_list2, reverse=True))
print(my_list2)

# 方法二 使用set去重
# 列表拼接
list3 = list1 + list2
# 列表去重
list4 = set(list3)  # {0, 34, 4, 11, 45, 16, 51, 23, 90}
list5 = list(list4)
print(sorted(list5, reverse=True))
