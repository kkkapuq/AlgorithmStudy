n, m = map(int, input().split())
numList = list(map(int, input().split()))

start = 0
end = 1
cnt = 0

while end <= n and start <= end:
    sumNum = numList[start:end]
    totalSum = sum(sumNum)
    
    if totalSum == m:
        cnt += 1
        end += 1
    elif totalSum < m:
        end += 1
    else:
        start += 1
        
print(cnt)