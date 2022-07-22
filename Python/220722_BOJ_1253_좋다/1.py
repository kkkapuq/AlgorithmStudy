'''
1. 투포인터를 사용해보자. 일단 들어온 수를 정렬시켜준다.
2. 정렬시키고 for문을 도는데, 이 때 i보다 큰 수는 고려하지 않는다.
'''
'''

# 투포인터 풀이
n = int(input())
numList = list(map(int, input().split()))

numList.sort()
cnt = 0

for i in range(len(numList)):
    tempList = numList[:i] + numList[i+1:]
    left = 0
    right = len(tempList) - 1
    
    while left < right:
        temp = tempList[left] + tempList[right]
        if temp == numList[i]:
            cnt += 1
            break
        elif temp > numList[i]:
            right -= 1
        else:
            left += 1

print(cnt)
'''

# 이진탐색 풀이
n = int(input())
numList = list(map(int, input().split()))

numList.sort()
cnt = 0

for i in range(len(numList)):
    tempList = numList[:i] + numList[i+1:]
    left = 0
    right = len(tempList) - 1
    mid = (left + right) / 2
    
    while left < right:
        temp = tempList[left] + tempList[right]
        if temp == numList[i]:
            cnt += 1
            break
        elif temp > numList[i]:
            right -= 1
        else:
            left += 1

print(cnt)