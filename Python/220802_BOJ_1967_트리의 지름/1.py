'''
1. 가중치가 있으므로 dfs로 풀어준다.
2. 가중치는 root와 leaf쪽에 배열 형태로 저장을 해주자
3. 최하단 노드의 가중치를 모두 더하면 그게 지름임ㅋ
'''

import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = [ [] for _ in range(n+1) ]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    root, leaf, cnt = map(int, sys.stdin.readline().split())
    graph[leaf].append([root, cnt])
    graph[root].append([leaf, cnt])
    
def dfs(v, weight):
    visited[v] = True
    
    for i in graph[v]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight + b
            visited[a] = True
            dfs(a, weight + b)
    
distance = [-1 for _ in range(n+1) ]
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1 for _ in range(n+1) ]
distance[start] = 0
dfs(start, 0)

print(max(distance))