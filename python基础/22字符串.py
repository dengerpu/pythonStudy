# 可以用单引号，也可以双引号，也可以三引号
# 单引号
name = 'dengerpu'
print(name, type(name))

# 双引号
name1 = "dengerpu1"
print(name1, type(name1))

# 三引号
name2 = '''
    abcabc
    abc
 '''
print(name2, type(name2))
name3 = """abcdefg"""
print(name3, type(name3))

# 如果字符串本身包含单引号，使用双引号定义，如果包含双引号可以使用单引号定义，或者统一使用三引号
my_name = "my name is 'dengerpu'"
print(my_name)
# python字符串乘以整数，代表复制几份
# 字符串 * num
print('hello'*3)
print('*'*10)

high = 160.5
print(F"身高：{high:.2f}")
# 两个{{}}会被换成一个花括号,不表示表达式
print(F"身高：{{high}}")