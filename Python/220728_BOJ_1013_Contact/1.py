import re

t = int(input())
for _ in range(t):
    tempStr = input()
    vega = re.compile('(100+1+|01)+')
    answer = vega.fullmatch(tempStr)
    if answer:
        print('YES')
    else:
        print('NO')