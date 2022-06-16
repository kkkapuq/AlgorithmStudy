import sys

n, m = map(int, input().split())
graph = [ [] for _ in range(n + 1)]
visited = [ False * 2 for _ in range(m) ]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

print(graph)
print(visited)