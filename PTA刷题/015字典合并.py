# 输入用字符串表示两个字典，输出合并后的字典。字典的键用一个字母或数字表示。注意：1和‘1’是不同的关键字！
#
# 输入格式:
# 在第一行中输入第一个字典字符串；
#
# 在第二行中输入第二个字典字符串。
#
# 输出格式:
# 在一行中输出合并的字典，输出按字典序。
#
# "1" 的 ASCII 码为 49，大于 1，排序时 1 在前，"1" 在后。其它的字符同理。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# {1:3,2:5}
# {1:5,3:7}
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# {1:8,2:5,3:7}
# 输入样例2:
# 在这里给出一组输入。例如：
#
# {"1":3,1:4}
# {"a":5,"1":6}
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# {1:4,"1":9,"a":5}
my_dict1 = eval(input())
my_dict2 = eval(input())
my_dict3 = {}
for key1, value1 in my_dict1.items():
    for key2, value2 in my_dict2.items():
        if key1 == key2:   # 将两个字典键值相同的的挑出来加到一起
            my_dict3[key1] = int(value1) + int(value2)
        if key1 not in my_dict3:
            my_dict3[key1] = value1
        if key2 not in my_dict3:
            my_dict3[key2] = value2
# ord()函数是Python中的一个库函数,用于从给定字符值中获取数字值,它接受一个字符并返回一个整数,即用于将字符转换为整数,即用于获取ASCII给定字符的值。
my_dict3 = dict(sorted(my_dict3.items(), key=lambda x: x[0] if type(x[0]) == int else ord(x[0])))
# ASCII码 0-9:48-57   a-z：97-122  A-Z：65-90
print(str(my_dict3).replace(' ', '').replace("'", '"'))  # 空格去掉，单引号要变成双引号



