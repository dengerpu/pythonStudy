# 幼儿园的老师给几位小朋友等量的长方体橡皮泥，但有个小朋友（小霸王）觉得自己的橡皮泥少了，就从另一个小朋友那里抢了一些。请问，是哪个小霸王抢了哪个小朋友的橡皮泥？
#
# 输入格式:
# 测试数据有多组。对于每组测试，首先输入一个整数n（n≤500），然后输入n行，每行包括3个不超过1000的整数l、w、h和1个字符串name（不超过8个字符且不含空格），其中，l、w、h分别表示橡皮泥的长、宽、高，name表示小朋友的姓名。当n等于-1时，输入结束。
#
# 输出格式:
# 对于每组测试，按“name1 took clay from name2.”的格式输出一行，其中name1代表小霸王的名字，name2代表被抢小朋友的名字，具体参考输出样例。
#
# 输入样例:
# 3
# 10 10 2 Jill
# 5 3 10 Will
# 5 5 10 Bill
# -1
# 输出样例:
# Bill took clay from Will.

while True:
    n = int(input())
    if n == -1:
        break
    my_dict = {}
    for i in range(n):
        value = input()
        value = value.split()
        long = int(value[0])
        width = int(value[1])
        height = int(value[2])
        name = value[3]
        my_dict[name] = long*width*height
    result = 0
    for value in my_dict.values():
        result += value
    aver = result / len(my_dict.values())
    for key,value in my_dict.items():
        if value > aver:
            name1 = key
        if value < aver:
            name2 = key
    else:
        print(f'{name1} took clay from {name2}.')

