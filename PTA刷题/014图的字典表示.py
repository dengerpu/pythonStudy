# 图的字典表示。输入多行字符串，每行表示一个顶点和该顶点相连的边及长度，输出顶点数，边数，边的总长度。比如上图0点表示：
# {'O':{'A':2,'B':5,'C':4}}。用eval函数处理输入，eval函数具体用法见第六章内置函数。
#
# 输入格式:
# 第一行表示输入的行数
# 下面每行输入表示一个顶点和该顶点相连的边及长度的字符串
#
# 输出格式:
# 在一行中输出顶点数，边数，边的总长度
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 4
# {'a':{'b':10,'c':6}}
# {'b':{'c':2,'d':7}}
# {'c':{'d':10}}
# {'d':{}}
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 4 5 35
n = int(input())
my_list = []
for i in range(n):
    value = eval(input())
    my_list.append(value)
# print(my_list)
edge_count = 0
total = 0
for dict_item in my_list:
    edge_count += len(dict_item[list(dict_item.keys())[0]])  # 字典第一个元素  (先获取key值，然后转为列表)
    for length in dict_item[list(dict_item.keys())[0]].values():
        total += int(length)
print(n, edge_count, total)