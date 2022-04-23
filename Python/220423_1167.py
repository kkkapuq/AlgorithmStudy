from collections import deque
    
#N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로의 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    #가장 오른쪽 아래까지의 최단거리 변환
    return graph[n-1][m-1]

#BFS를 수행한 결과 출력
print(bfs(0, 0))

from collections import deque

n, m = map(int, input().split())

#2차원 리스트에 공백없이 할당
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#상하좌우 움직이는 값 정의    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        #현재 위치로부터 상하좌우 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #지정범위 초과라면 무시하고 다음꺼 확인
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #괴물을 만난다면 다른곳 체크
            if graph[nx][ny] == 0:
                continue
            #괴물이 없는 곳이라면 방문처리, 이동할 좌표값을 +1 해주기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))
