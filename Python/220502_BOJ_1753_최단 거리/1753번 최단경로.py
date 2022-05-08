# https://www.acmicpc.net/problem/1753
# 다익스트라 알고리즘 - 하나의 정점에서 나머지 모든 정점까지의 최단 거리를 찾는 알고리즘

# deque에는 리스트가 append되지 않는다...
# from collections import deque
import sys
import heapq

# 정점의 개수 V와 간선의 개수 E
v, e = map(int, input().split())
start = int(input())
INF = sys.maxsize
heap = []
graph = [[] for _ in range(e + 1)]
answer_wei = [INF] * (v + 1)

for i in range(e):
    # a에서 b로 가는 가중치 c인 간선이 존재
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

# heap == 이진 트리?  리스트랑 다른점은?
# 너비우선탐색과 거의 비슷한듯
def stra(start):
    answer_wei[start] = 0
    # heap 초기화
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)
        # print(f"wei {wei}, now {now}")

        if answer_wei[now] < wei:
            continue

        for w, next_val in graph[now]:
            next_wei = w + wei
            if next_wei < answer_wei[next_val]:
                answer_wei[next_val] = next_wei
                heapq.heappush(heap, (next_wei, next_val))

stra(start)
for i in range(1, v + 1):
    print("INF" if answer_wei[i] == INF else answer_wei[i])
