# 开发人：陶倩
# 开发时间： 2023/3/24  17:14
d = {
    '-': 'fu',
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu',
}
s = list(input())
for i in range(len(s) - 1):
    print(d[s[i]] + ' ', end='')
print(d[s[len(s) - 1]], end='')


