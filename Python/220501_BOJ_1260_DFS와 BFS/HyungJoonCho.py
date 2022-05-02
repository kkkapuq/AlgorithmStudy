from collections import deque 

def dfs(graph, v, visited):
    # v번째 노드 방문처리
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        # 방문하지 않았다면, 재귀로 dfs 실행
        if visited[i] == 0:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    # dfs 에서 썼으니까 초기화 다시해주기
    visited = [0] * (n + 1)
    queue = deque([v])
    # v번째 노드 방문처리
    visited[v] = 1
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        # x번 노드에 연결된 정보 확인
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [ [] for _ in range(n + 1) ]
visited = [0] * (n + 1)

# 1번부터 n번까지 각 노드별 연결정보 삽입, 작은 노드부터 탐색해야 되니까 정렬해주자
for i in range(1, m + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()
    
dfs(graph, v, visited)
print()
bfs(graph, v, visited)
