def is_tangible(a, b, c):
    if a<0 or b<0 or c<0:
        raise Exception('三角形的边不能为负数')
    if a+b>c and a+c>b and b+c>a:
        print(f'能构成三角形，三角形的边长为a={a}，b={b},c={c}')
    else:
        print(f'a={a}，b={b},c={c}不能构成三角形')


if __name__ == '__main__':
    try:
        a = int(input('请输入第一条边：'))
        b = int(input('请输入第二条边：'))
        c = int(input('请输入第三条边：'))
        is_tangible(a, b, c)
    except Exception as e:
        print(e)