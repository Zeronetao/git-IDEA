# 开发人：陶倩
# 开发时间： 2023/8/14  8:38
#某公司员工的工资计算方法如下：一周内工作时间不超过40小时，按正常工作时间计酬；超出40小时的工作时间部分，按正常工作时间报酬的1.5倍计酬。
#员工按进公司时间分为新职工和老职工，进公司不少于5年的员工为老职工，5年以下的为新职工。
#新职工的正常工资为30元/小时，老职工的正常工资为50元/小时。
#请按该计酬方式计算员工的工资。

year, time = input().split(' ')

year = float(year)
time = float(time)

#计算老员工正常工作时间工资
if year >= 5 and time < 40:
    money = 50 * time
    print("%.2f" %money)

#计算老员工加班时间工资
if year >= 5 and time >= 40:
    money = 50 * 40 + 75 * ( time - 40)
    print("%.2f" % money)

#计算新员工正常时间工资
if year < 5 and time < 40:
    money = 30 * time
    print("%.2f" % money)

#计算老员工加班时间
if year < 5 and time >= 40:
    money = 30 * 40 + 45 * ( time - 40)
    print("%.2f" % money)