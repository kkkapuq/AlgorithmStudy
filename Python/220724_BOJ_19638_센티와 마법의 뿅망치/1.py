'''
1. 최대 힙 사용, -로 변형시켜서 풀이
2. 마지막엔 giantList의 0번째 인덱스의 절댓값이 센티의 키보다 작아야 하므로 -giantList[0] 해주자.
'''

import sys
import heapq

n, h, t = map(int,(input().split()))

giantList = []
cnt = 0

for i in range(n):
    heapq.heappush(giantList, -int(sys.stdin.readline().rstrip()))

for i in range(t):
    v = heapq.heappop(giantList)
    if -v < h:
        heapq.heappush(giantList, v)
        break
    elif -v == 1:
        heapq.heappush(giantList, v)
    else:
        temp = -(-v // 2)
        heapq.heappush(giantList, temp)
        cnt += 1

if -giantList[0] < h:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(-heapq.heappop(giantList))