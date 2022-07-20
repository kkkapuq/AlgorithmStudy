'''
1. bfs로 사용해보자, 집을 돌면서 방문한 집은 0으로 처리해주는데, 상하좌우 탐색결과 집이 있으면 단지 내 아파트 수인 cnt에 집 수만큼 더해주자.
2. dfs도 동일한 방식으로 진행하면 될듯?
'''

import sys
from collections import deque

n = int(input())
graph = []
answer = []
visited = [ [False] * n for _ in range(n) ]
cnt = 0
result = 0

# 상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

def dfs(graph, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph, nx, ny)
        return True
    return False
            
        

for _ in range(n):
    tempList = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(tempList)

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             answer.append(bfs(graph, i, j))

for i in range(n):
    for j in range(n):
        if dfs(graph, i, j):
            answer.append(cnt)
            cnt = 0
        
answer.sort()
print(len(answer))
for i in answer:
    print(i)
