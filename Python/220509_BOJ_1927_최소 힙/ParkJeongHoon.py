import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

hq = []
for _ in range(n):
    temp = int(input().rstrip())
    
    if temp == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, temp)
