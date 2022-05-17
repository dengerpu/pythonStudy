while True:
    try:
        height = float(input('请输入身高：'))
        weight = float(input('请输入体重：'))
        bmi = weight / (height + weight)
        print(f'你的身高是：{height}')
        print(f'你的体重是：{weight}')
        print(f'你的BMI的指数是：{bmi}')
        break
    except:
        print('输入不合法')
