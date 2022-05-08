# https://www.acmicpc.net/problem/1260
from collections import deque

# 정점의 개수, 간선의 개수, 탐색 시작 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer_bfs = [v]
answer_dfs = []

for _ in range(0, m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()
# print(graph)

# bfs(Breadth-first-Search) 너비우선 탐색 사용
def bfs():
    deq = deque([v])
    while(deq):
        val = deq.popleft()
        for next_val in graph[val]:
            if next_val not in answer_bfs:
                answer_bfs.append(next_val)
                deq.append(next_val)
            else:
                pass

# 깊이 우선 탐색
visited = [False] * (n + 1)
def dfs(val):
    visited[val] = True
    answer_dfs.append(val)
    for next_val in graph[val]:
        if not visited[next_val]:
            dfs(next_val)


dfs(v)
print(answer_dfs)

bfs()
print(answer_bfs)
