num = 10


def anum():
    # global num
    num = 20


anum()
print(num)  # 输出是10，要想改变num的值，应该用global
# 对于在函数内部的变量，如果改变没有global声明的变量，那么相当于是重新定义了一个与全局变量同名的局部变量


def abnum(big, small, middle):
    print(f'big:{big},small:{small},middle:{middle}')


abnum(small=2, big=1, middle=3)



# 在填写个人资料时，如果选了女性，那么性别是女；
# 如果不选性别，那就是默认是男，那么这个功能用函数怎么实现？
# 要求如下：定义一个函数gender，并在函数中将“所选性别为*”，并可以成功调用运行。


def gen(gender = '男'):
    print(f'所选性别为：{gender}')


gen()
gen('女')


# 要求实现一段代码：
# 声明一个函数num，并且在调用函数的时候，不管输入多少个非关键字参数，
# 函数都可以运行，且在函数内部还要把每个参数输出到屏幕上。
def pr(*args):
    print(args)


pr(1, 2, 3)


# 如下所示这是一个字典，{"name":"电脑","price":7000}
# 请定义这样一个函数num，讲上述字典中的键值对传入到函数num中，
# 要求用不定长参数来接收，并在函数中打印键值对输出
def num(**kwargs):
    for k,v in kwargs.items():
        print("key:", k, "value:", v)
    # for value in kwargs.values():
    #     print(f'key: price value: {value}')

num(name = "电脑", price = 7000)


# 对于一个函数num，当调用nun(1,2,a=3,b=4)和
# 调用num(3,4,5,6,a=1)以及
# num(a=1,b=2)的时候都可以正常运行，
# 并且可以对元组以及字典类型进行遍历输出，
# 对字典类型进行输出字典的键值对(形式为：key：a，value：1)，
# 请写出这个函数并完成调用。
def num(*args, **kwargs):
    for i in args:
        print(i,end=' ')
    print()
    for k, v in kwargs.items():
        print("key:", k, "value:", v)


num(1,2,a=3,b=4)
num(3,4,5,6,a=1)
num(a=1,b=2)

num = 3.14
print(f'{num:.3f}')
num1 = 1
print("num:%6d" % num1)
print("num:%06d" % num1)
print(f'{num1:06d}')


