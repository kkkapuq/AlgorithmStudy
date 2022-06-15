'''
1. 랜선 리스트를 만들고, 그 안에서 for문 돌면서 이진탐색 처음과 끝 설정해주자
2. 가장 짧은놈을 start, 긴놈을 end로 두자
3. 목표치 설정은.... 총 길이의 절반(mid)으로 두고..
4. 현재 잘라낸 길이가 < mid 면 start = mid + 1, > mid 면 end = mid -1
5. 근데 언제까지 잘라내지?
6. 시간복잡도는 정렬 1회에 start~end만큼 도니 NlogN 인가?
'''
import sys

k, n = map(int, input().split())

cableList = [ ]

for _ in range(k):
    cableList.append(int(sys.stdin.readline()))
    
cableList.sort() # 이진탐색은 정렬이 되어있어야함.
start, end = 1, max(cableList)

while start <= end:
    mid = (start + end) // 2 # 나머지는 버려주니까 // 사용
    cnt = 0
    
    for i in range(k):
        cnt += cableList[i] // mid # 선을 mid로 나눈 몫만큼 선이 생기니까 나눈 몫만큼 cnt 더해주기
        
    if cnt >= n: # 잘라낸 선이 n보다 많이 나와버리면 안됨 start + 1 해주고 다시 while문 돌자
        start = mid + 1
    else: # 아니라면 끝을 줄여주기
        end = mid - 1

print(end)