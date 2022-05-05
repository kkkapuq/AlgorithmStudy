import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v + 1)]
heap = [] #거리가 작은 것부터 연산하는것이 다익스트라에서 좋다고 들었다 그러므로 힙을 사용할것이다.
answer = [sys.maxsize] * (v + 1)

def dijkstra(node):
    answer[node] = 0
    heapq.heappush(heap, (0, node))

    while heap:
        val, now = heapq.heappop(heap)

        if answer[now] < val:
            continue

        for w, next_node in graph[now]:

            next_wei = w + val

            if next_wei < answer[next_node]:
                answer[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))



for i in range(e):
    start, end, value = map(int, input().split())
    graph[start].append((value, end))

dijkstra(k)
for i in range(1,v + 1): 
    print("INF" if answer[i] == sys.maxsize else answer[i])
