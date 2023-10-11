# 开发人：陶倩
# 开发时间： 2023/3/24  15:54
num = int(input())
assert 0 <= num

def jisuan( num ):
    for i in range(0,10):
        j = str(num).count(str(i))
        if j != 0:
            print("%d:%d"%(i,j))

jisuan( num )