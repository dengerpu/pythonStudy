import datetime


def inputdate():
    indate = input('请输入开始日期（20200808）后按回车：')
    indate = indate.strip()
    datestr = indate[0:4]+'-'+indate[4:6]+'-'+indate[6:]
    return datetime.datetime.strptime(datestr,'%Y-%m-%d')


print('------------推算几天后的日期----------------')
sdate = inputdate()
in_num = int(input('请输入间隔天数：'))
fdate = sdate + datetime.timedelta(days=in_num)
print('你推算的日期是：'+str(fdate))