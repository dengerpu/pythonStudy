# if判断的基本格式
# if 判断条件:
#     判断条件为True,会执行的代码

# 顶格书写的代码，代表和if判断没有关系
# 在python中使用缩进，代替代码的层次关系，在if语句的缩进内，属于if语句的代码块

age = int(input('请输入你的年龄:'))

if age >= 18:
    print("您的年龄大于等于18岁可以进入网吧")
else:
    print("未满18岁，不可以进入")
print("判断结束")
# if 判断条件:
#     判断条件为True，会执行的代码
# else:
#     判断条件为Flase,会执行的代码
# if和else只会执行其中的一个

# if 判断条件1:
#     判断条件1成立，执行代码
# elif 判断条件2:
#     判断条件1不成立，判断条件2成立，会执行的代码
# else:
#     判断条件1和判断条件2都不成立，之行的代码

score = eval(input('请输入你的成绩'))

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
   print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# if 判断条件1:
#     判断条件1成立，会执行的代码
#     if 判断条件2:
#         判断条件1成立，判断条件2成立会执行的代码
#     else:
#         判断条件1成立，判断条件2不成立执行的代码
# else:
#     判断条件1不成立，会执行代码

money = int(input('请输入你的零钱'))

if money >= 2:
    print("我上车了")
    seat = int(input('车上的空位个数:'))
    if seat >= 1:
        print("有座位坐")
    else:
        print("没有座位，只能站着")
else:
    print("没钱，只能走路")
