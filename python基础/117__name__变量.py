import my_calc # 模块的导入，会执行模块中的代码

my_calc.add(100, 200)

print(__name__)

if __name__ == '__main__':
    print('我会自动执行')