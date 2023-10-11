# 开发人：陶倩
# 开发时间： 2023/8/14  9:18

Open , High , Low , Close = input().split(' ')

Open = float(Open)
High = float(High)
Low = float(Low)
Close = float(Close)

if Close < Open :
    print("BW-Solid", end='')
if Close > Open :
    print("R-Hollow", end='')
if Close == Open :
    print("R-Cross", end='')

if Low < Open and Low < Close :
    if High > Open and High > Close :
        print(" with Lower Shadow and Upper Shadow")
    else:
        print(" with Lower Shadow", end='')

elif High > Open and High > Close :
    print(" with Upper Shadow")