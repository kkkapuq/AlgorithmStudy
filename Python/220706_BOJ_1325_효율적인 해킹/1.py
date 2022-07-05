'''
1. 꼬리에 꼬리를 물고 신뢰관계인 다른 컴퓨터까지 해킹이 가능하니, DFS인것 같은데 DFS로 해보자.
2. 신뢰관계를 입력받을 때, N번 노드의 신뢰관계 정보를 담은 graph 의 N번 인덱스에 신뢰하는 노드를 넣어주자.
3. start를 1부터 하고, dfs 한 사이클이 끝날 때, cntList의 n번째 인덱스에 방문 가능한 총 개수를 입력...
4. 그중 max 뽑아주자.
----------------
1. ㅈㅈ. DFS로 안풀리는거같음.. BFS로 시도해보자
2. BFS 함수 내에서 visited를 초기화 시켜줘야 한다. visited 밖으로 꺼내놓고 쓰려니까 머리아픔 제대로 되는거같지도않고
'''
from collections import deque

def bfs(v):
    visited = [False] * (n+1)
    visited[v] = True
    
    q = deque([v])
    cnt = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt


n, m = map(int, input().split())

graph = [ [] for _ in range(n+1)]
cntList = []
max = -1

# b를 해킹했을 때 a까지 해킹되야 되므로, graph[a]에는 b를 넣어주지 않는다.
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max:
        cntList = [i]
        max = cnt
    elif cnt == max:
        cntList.append(i)
        
print(" ".join(map(str, cntList)))