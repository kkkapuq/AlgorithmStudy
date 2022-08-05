'''
1. 가짓수를 나타내는 dp[0, 0, 0 ... ] list 생성
2. 0원으로 만드는 가짓수는 무조건 1개 있으므로 d[0]은 1 해주고..
3. 만들고자 하는 금액 j 가 현재 동전 i 보다 크다면, j에서 i를 빼준 값 dp[j-i] 를 dp[j] 에 더해준다 (가짓수 추가)
'''

from itertools import combinations

t = int(input())

for _ in range(t):
    n = int(input())
    coinList = list(map(int, input().split()))
    m = int(input())
    
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    
    for i in coinList:
        for j in range(m+1):
            if j >= i:
                dp[j] += dp[j-i]
                
    print(dp[m])