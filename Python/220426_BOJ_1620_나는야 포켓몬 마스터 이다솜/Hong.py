# https://www.acmicpc.net/problem/1620

import sys

n, m = map(int, input().split())

dicName = {}
dicNum = {}
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    dicName[i] = name
    dicNum[name] = i

for i in range(m):
    answer = sys.stdin.readline().strip()
    if answer.isdigit():
        print(dicName[int(answer)])
    else:
        print(dicNum[answer])
