# 开发人：陶倩
# 开发时间： 2023/3/24  16:38

N = int(input())

assert 0 <= N <= 1000

student = []

for i in range(0, N):
    student.append(list(input().split(' ')))

M = int(input())

testSeatNumber = []

testSeatNumber.extend(list(input().split(' '))) #随后一行中给出 M 个待查询的试机座位号码，以空格分隔

for j in testSeatNumber :   #j依次取需要查询的试机号码

    for i in student :      #i依次取每个学生的信息

        if j == i[1] :      #将需要查询的试机号码与每个学生的信息中的试机号码对比，若一样输出结果

            print("{} {}".format(i[0], i[2]))   #输出对应考生的准考证号i[0]和考试座位号码i[2]
