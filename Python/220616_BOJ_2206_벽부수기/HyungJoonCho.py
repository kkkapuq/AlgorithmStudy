'''
1. 벽을 부술지 말지 판단하는건 어떻게 하지?
2. flag 값을 두고, 방문했을 때 상하좌우 탐색해서 벽 부술 수 있는지 판단
3. dfs 사용하기
'''

import sys

n, m = map(int, input().split())
graph = [ [] for _ in range(n + 1)]
visited = [ False * 2 for _ in range(m) ]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

print(graph)
print(visited)