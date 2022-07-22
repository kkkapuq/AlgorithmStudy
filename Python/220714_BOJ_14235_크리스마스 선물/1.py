'''
1. 우선순위 큐를 사용한다.
2. 가치가 가장 큰 선물을 줘야되니까, heappush할 때 -1 곱해서 넣어주고, heappop할 때 -1 곱해서 원상복구 시켜준다 (최대힙)
'''

import heapq
import sys

n = int(input())

q = []

for i in range(n):
    tempList = list(map(int, sys.stdin.readline().split()))
    if tempList[0] == 0:
        if len(q) < 1:
            print(-1)
        else:
            print(-heapq.heappop(q))
    else:
        for j in range(1, len(tempList)):
            heapq.heappush(q, -1*tempList[j])