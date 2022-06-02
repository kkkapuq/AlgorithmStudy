import heapq
import sys

n = int(input())
maxHeap = []
for i in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(maxHeap, -x)
    else:
        if len(maxHeap) < 1:
            print(0)
        else:
            print(-1 * heapq.heappop(maxHeap))
