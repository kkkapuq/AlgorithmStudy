import sys
from collections import deque

n = int(input())
dp = deque()

for i in range(n):
    dp.append(deque(map(int, sys.stdin.readline().split())))
    dp[i].append(0)
    dp[i].appendleft(0)

for i in range(1, n):
    for j in range(1, i + 2):
        dp[i][j] = max(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j])


print(max(dp[-1]))