'''
1. 최소힙을 이용하고, 힙 안에 있는 원소들이 K이상이라면 for문 종료
2. 힙은 push, pop 할때마다 정렬해주므로.. 맨 처음 원소가 K이상이라면 while문 빠져나오면될듯하다
'''
import heapq

def solution(scoville, K):
    answer = 0
    
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
        
    while heap[0] < K:
        temp = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        heapq.heappush(heap, temp)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    
    return answer