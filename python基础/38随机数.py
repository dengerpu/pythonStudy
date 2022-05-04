import random

# random.randint(a, b) ，返回 [a, b] 之间的整数，包含 a 和 b

for i in range(1,10):  # [1,10)  1 2 3 4 5 6 7 8 9
    num = random.randint(1,100)  # 返回【1,100】之间的整数
    print(num)

for i in range(5):
    print(i)
# 这里和C语言有区别
print('最后结果是%d ' % i)

# break/continue只能用在循环中，除此以外不能单独使用
#
# break/continue在嵌套循环中，只对最近的一层循环起作用

