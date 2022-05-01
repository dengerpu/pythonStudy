# if else结构变形
# if 判断条件:
#     表达式1
# else:
#     表达式2

# 变量 = 表达式1 if 判断条件 else 表达式2
# 变量最终存储的结构是：
#     判断条件成立，表达式1的值
#     条件不成立，表达式2的值

a = int(input('请输入一个数字：'))
b = int(input('请输入一个数字：'))

result = (a-b) if a > b else (b-a)
print(result)
