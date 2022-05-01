for i in 'hello':  # 循环遍历字符串中的每个字符
    print(i)

# range(n)  会生成[0,n)的数据序列，不包含n
for i in range(5):  # 0,1,2,3,4
    print(i)

# range(a,b) 会生成[a, b)的整数序列，不包含b
for i in range(5,10):
    print(i)

# range(a, b, step)会生成[a, b)的整数序列，但是每个数字之间的间隔是step

for i in range(1, 10, 3):
    print(f"有间隔的{i}")