N, S = map(int,input().split())
nums = list(map(int,input().split()))
i, j = 0, 0
s = nums[0]
ans = 100001
 
while True:
    if s >= S:
        s -= nums[i]
        ans = min(ans, j - i + 1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        s += nums[j]
 
if ans == 100001:
    print(0)
else:
    print(ans)
