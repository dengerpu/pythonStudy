# 给定一组整数，还有一个目标数，在给定这组整数中找到两个数字，使其和为目标数，如找到，解是唯一的。找不到则显示 "no answer"。输出的下标按从小到大排序。用一重循环加字典实现。
#
# 输入格式:
# 在一行中给出这组数。
# 在下一行输入目标数
#
# 输出格式:
# 在一行中输出这两个数的下标，用一个空格分开。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# 2,7,11,15
# 9
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# 0 1
# 输入样例2:
# 在这里给出一组输入。例如：
#
# 3,6,9
# 10
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# no answer
num_list = list(map(int, input().split(',')))
sum = int(input())
my_dict = {}
for i in num_list:  # 字典中保存对应的差值（键+值 = sum）
    my_dict[i] = sum - i
for key, value in my_dict.items():
    if key in num_list and value in num_list:
        print(num_list.index(key), num_list.index(value))
        break
else:  # 正常结束执行
    print('no answer')
