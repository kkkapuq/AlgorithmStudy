import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    
    return False

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())

    #n줄만큼 m의 갯수만큼 0 (빈 땅) 생성
    graph = [ [0]*m for _ in range(n)]
    
    #배추를 심을 자리 정해주기
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    #dfs 탐색 실행
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
            
    print(cnt)