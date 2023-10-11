# 开发人：陶倩
# 开发时间： 2023/3/24  17:35
a, b = input().split()
a = int(a)
b = int(b)

assert -100 <= a and a <= b and b<=100

count = 0

alist = []

for i in range(a, b+1):
    if count %5 == 0 and count != 0:
        print()
    print("{: >5}".format(i), end=" ")  #取位对齐
    count = count + 1
    alist.append(i)

print("\nSum = ", sum(alist), end=" ")
