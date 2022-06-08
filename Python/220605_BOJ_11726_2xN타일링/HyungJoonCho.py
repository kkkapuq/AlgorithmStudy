'''
1. 방법의 수? 
2. 10007은 왜 나누라는거임?
n = 1 -> 1
n = 2 -> 2
n = 3 -> 3
n = 4 -> 5
n = 5 -> 8

f(n) = f(n-1) + f(n-2)
'''
'''
# 시간초과 나는 풀이

import sys
sys.setrecursionlimit(10000)

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return dp(n-1) + dp(n-2)

n = int(input())

print((dp(n)%10007))
'''
n = (int(input()))

dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)
