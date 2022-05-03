# my_str.replace(old_str,new_str,count) 字符串的替换，将my_str中的old_str替换为new_str
# old_str：将要被替换的字符串
# new_str: 新的字符串，替换成的字符串
# count 替换的次数，默认是全部替换
# 返回值，得到一个新的字符串，不会改变原来的字符串

my_str = 'hello world itcast and itcastcpp'

print(my_str.replace('itcast','dengerpu'))

# 替换一次
print(my_str.replace('itcast', 'dengerpu', 1))