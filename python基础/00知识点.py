# # 标识符命名规则：由数字，字母，下划线组成，不能以数字开头
# # 变量名不能和关键词重复
# # 关键字是系统定义好的标识符，具有特殊的作用
# # 数据类型 int(整数) float(浮点数) str(字符串) bool(布尔类型 True False)
# list(列表) tuple(元组) dict(字典)
#
# type() 函数可以查看变量的数据类型
# 输入：input() --> str 类型转换 int() float() eval()
# 输入：print() %s--字符串 %d--整数 %f--浮点数 %--%%
#     f-string{变量}
#
# 逻辑运算符
#     and 逻辑与 一假为假
#     or  逻辑或 一真为真
#     not 逻辑非 取反
# 比较运算符
#     == ！=
# 判断 if elif else
# 循环 while
#     for x in 容器/range():
#         pass
#     range(a, b ,step) [a, b)之间的整数
#     break 终止循环
#     continue 跳过本次循环，继续下次循环
#     循环 else 结构：循环不是被break终止的时候会执行else中的代码
#
# str 下标 切片 [:]拷贝 [::-1]逆置
#
# list: insert append extend
# tuple: 元组中的数据不能修改  查询 index()
# dict: key:value 键值对的形式
#
# 函数：
# 定义： def 函数名（）：
#          函数代码
#          return 数据
# 函数调用，才会执行函数中的代码
# 函数名（实参列表）
# 局部变量：在函数内部定义的变量，只在当前函数内部使用，如果想要将这个变量在函数外部使用
#         1.可以使用return将这个变量返回 2.使用global设为全局变量
# 全局变量：在任意地方都可以访问，想要在函数内部修改全局变量的值，使用global