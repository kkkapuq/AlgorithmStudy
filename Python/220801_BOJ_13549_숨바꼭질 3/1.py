'''
1. 다익스트라 기본문제... BFS로도 풀수있으니 일단 BFS로 풀어보자
2. 다익스트라로 푼다면 INF 100001로 설정해주고, 우선순위 큐를 사용할것.... (heapq)
'''

from collections import deque
import heapq
import sys

n, k = map(int, (input().split()))
cnt = 0
INF = 100001
visited = [False for _ in range(INF)]
dist = [-1 for _ in range(INF)] 
visited[n] = True
dist[n] = 0


def bfs():
    q = deque()
    q.append(n)
    
    while q:
        v = q.popleft()
        # 순간이동
        if 0 <= v * 2 < INF and visited[v*2] == False:
            q.append(v*2)
            visited[v*2] = True
            dist[v*2] = dist[v]
        # x-1 이동
        if 0 <= v-1 < INF and visited[v-1] == False:
            q.append(v-1)
            visited[v-1] = True
            dist[v-1] = dist[v] + 1
        # x+1 이동
        if 0 <= v+1 < INF and visited[v+1] == False:
            q.append(v+1)
            visited[v+1] = True
            dist[v+1] = dist[v] + 1
            
    print(dist[k])
bfs()
        
    
    
# from collections import deque
# MAX = 100001
# check = [False] * MAX
# dist = [-1] * MAX

# n,k = map(int, input().split())
# q = deque()
# q.append(n)
# check[n] = True
# dist[n] = 0

# while q:
#     now = q.popleft()
#     if now*2 <= MAX and check[now*2] == False:  # 순간이동
#         q.appendleft(now*2)
#         check[now*2] = True
#         dist[now*2] = dist[now]
#     if now + 1 <= MAX and check[now+1] == False: # x+1이동
#         q.append(now+1)
#         check[now+1] = True
#         dist[now+1] = dist[now] + 1
#     if now - 1 >= 0 and check[now-1] == False: # x-1이동
#         q.append(now-1)
#         check[now-1] = True
#         dist[now-1] = dist[now] + 1
# print(dist[k])