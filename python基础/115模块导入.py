"""
模块就是一个python文件，别人已经写好的代码可以直接使用
模块的名字要遵循标识符的规则（由字母，数字和下划线组成，不能以数字开头）
"""
# 方法一 import 模块名
# 使用 模块名.功能名
import my_module1
print(my_module1.num)
my_module1.fun()
dog = my_module1.Dog()
dog.cls()
dog.sta()

print('='*30)

# 方法二  from 模块名 import 功能名1， 功能名2.
# 如果存在同名方法名，则会覆盖
from my_module2 import num, fun as newfun
from my_module3 import num, Dog
print(num)
# fun()
newfun()
dog = Dog()
dog.cls()
dog.sta()

print('='*30)

# 方法3 from 模块名 import *   # 将模块的所有功能进导入

from my_module3 import *
print(num)
fun()
dog = Dog()
dog.cls()
dog.sta()

print('='*30)
# as 起别名，可以对模块和功能起别名
# 如果用as起别名，就不能再使用原来的名字
import my_module1 as m1
print(m1.num)
m1.fun()
dog = m1.Dog()
dog.cls()
dog.sta()