# 开发人：陶倩
# 开发时间： 2023/3/24  14:21
num, ch = input().split(' ')
# 字符的数量强制转换为整型
num = int(num)
# 沙漏任意一边的行数
row = 1
# 确定沙漏任意一边的行数
while (2 * row ** 2 - 1) <= num:
    row = row + 1

row = row - 1

long = 2 * row - 1

# 打印沙漏的中部和上部
for i in range(row, 0, -1):
    print((ch * (2 * i - 1)).rjust(long))
    long = long - 1

long = long + 1

# 打印沙漏的下部
for j in range(2, row + 1):
    long = long + 1
    print((ch * (2 * j - 1)).rjust(long))

# 输出剩余的符号数
print(num - 2 * row ** 2 + 1)