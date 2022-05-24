import sys
from collections import deque
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = 1
    global cnt
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

def bfs(v):
    visited[v] = 1
    q = deque([v])
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                global cnt
                cnt += 1
                q.append(i)

n = int(input())
m = int(input())
cnt = 0

visited = [0] * (n + 1)
graph = [ [] for _ in range(n + 1)]

# 간선정보 매핑
for _ in range(1, m + 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
print(cnt)