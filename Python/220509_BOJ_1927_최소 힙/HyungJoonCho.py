import sys
import heapq

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)