# 开发人：陶倩
# 开发时间： 2023/8/14  10:04

N , U ,D = input().split(" ")

N = int(N)
U = int(U)
D = int(D)

i=0
Height = 0
count = 0

while Height < N :
    Height = (i + 1) / 2 * U
    i =+ 1
    Height = Height - i / 2 * D
    i =+ 1

print("%d" %i)