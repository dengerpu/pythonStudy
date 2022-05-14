"""
__all__变量，可以在每个代码文件（模块中）定义，类型是元组或列表
作用：影响 from 模块名 import * 的导入行为，另外两种导入行为不受影响
1. 如果没有定义__all__变量，模块中的所有功能都可以被导入
2. 如果定义__all__变量，只能导入变量中定义的变量
"""
from my_module4 import *
print(num)
fun()
dog = Dog()
dog.cls()
dog.sta()


