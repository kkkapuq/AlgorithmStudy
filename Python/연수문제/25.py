n = int(input())

graph = [] 
visited = [False] * n
cnt = 0

def dfs(v):
    visited[v] = True
    global cnt
    for i in graph[v]:
        if visited[i] == False:
            cnt += 1
            dfs(i)

for i in range(n):
    temp = list(map(int, input().split()))
    temp.sort()
    graph.append(temp)
    
dfs(0)
print(cnt)