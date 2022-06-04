'''
1. 연결요소가 뭔지는 모르겠는데.. 연결된 노드들의 집합? 을 말하는거같음
2. 예제 1은 2개의 연결노드 집합이 있고, 예제 2는 1개로 다 연결되있는것같다.
3. 1번부터 n번노드까지 visited가 false 라면 cnt++ 해주자
'''
import sys
from collections import deque
sys.setrecursionlimit(10000)

# bfs, dfs 구현에 필요한 친구들 입력받는곳
n, m = map(int, input().split())
graph = [ [] for _ in range(n + 1) ]
visited = [False] * (n + 1)
cnt = 0

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

def bfs(v):
    visited[v] = True
    q = deque([v])
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True


# 간선정보 매핑
for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        #bfs(i)
        cnt += 1
        
print(cnt)