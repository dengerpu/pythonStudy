# 早期中国的居民身份证由15位数字后来组成。国务院决定自1999年10月1日起公民身份证号码由15位升至18位。
#
# 15位居民身份证号码是由15位得数字组成，排列顺序从左至右依次为：六位数字地址码，六位数字出生日期码（年份月份日期都是两位），三位数字顺序码。三位数字顺序码男性使用1、3、5、7、9等奇数，女性使用2、4、6、8、0等偶数。
# 18位居民身份证号码排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码（男性使用1、3、5、7、9等奇数，女性使用2、4、6、8、0等偶数）和一位数字校验码。
#
# 身份证号码可以用正则表达式判断是否合法，也可以用字符串判断来判断。
#
# 从键盘输入一串15位 或18位的字符串。
# 首先判断该字符串中表示日期的字符串是否符合日期字符串，若不符合则给出提示。
# 例如 输入：3501021990229403X， 则输出：Error,日期不合法
#
# 若日期合法则认为该字符符合中国的居民身份证编码（本题假设除了日期有可能输错，其他不会输错）
#
# 若输入字符是15位符合中国的居民身份证编码，则输出性别 与 以类似于“1990年10月01日”的形式的出生日期。
#
# 例如：输入350102901001402，则输出：女,1990年10月01日
#
# 若输入字符是18位符合中国的居民身份证编码，则输出性别 与 以类似于“2000年10月01日”的形式的出生日期。
#
# 例如：输入35010220001001403X，则输出：男,2000年10月01日
#
# {特别备注说明：本题考核点为字符串应用，在测试样例中给出否让身份证号码只符合上述规则，没有判断区号与验证码是否有意义，未经过身份证验证接口API（公安部实时接口)验证}
#
# 输入格式:
# 键盘读入一串字符串
#
# 输出格式:
# 输出相应的结果
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# 35010219990229401X
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# Error,日期不合法
# 输入样例2:
# 在这里给出一组输入。例如：
#
# 350102901001412
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# 女,1990年10月01日
# 输入样例3:
# 在这里给出一组输入。例如：
#
# 35010220001001403X
# 输出样例3:
# 在这里给出相应的输出。例如：
#
# 男,2000年10月01日
import datetime
card = input()
if len(card) == 15:
    try:
        birthday = card[6:12]
        year = '19' + birthday[0:2]
        month = birthday[2:4]
        day = birthday[4:6]
        datetime.date(int(year), int(month), int(day))
        gender = int(card[-1])
        if gender % 2 == 0:
            print(f'女,{year}年{month}月{day}日')
        else:
            print(f'男,{year}年{month}月{day}日')
    except Exception as e:
        print('Error,日期不合法')
elif len(card) == 18:
    try:
        birthday = card[6:14]
        year = birthday[0:4]
        month = birthday[4:6]
        day = birthday[6:8]
        datetime.date(int(year), int(month), int(day))
        gender = int(card[-2])
        if gender % 2 == 0:
            print(f'女,{year}年{month}月{day}日')
        else:
            print(f'男,{year}年{month}月{day}日')
    except Exception as e:
        print('Error,日期不合法')
