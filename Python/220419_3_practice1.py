#재귀 호출 한도 늘려주기
import sys
sys.setrecursionlimit(10**7)

#세로, 가로줄
n, m = map(int, input().split())

#2차원 리스트로 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] == 1
        #상, 하, 좌, 우 위치 모두 재귀적으로 호출
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print(result)