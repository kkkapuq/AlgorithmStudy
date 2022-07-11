'''
1. 특정 좌표의 상하좌우를 탐색하면서, 상하좌우 cnt의 합이 3 이상인 곳은 '.' 으로 바꿔준다.
2. 기존 지도를 deepcopy 한 newMap을 만들고, newMap의 사이즈를 조절하는게 핵심
'''
import copy
import sys

r, c = map(int, input().split())

m = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(r):
    m.append(list(map(str, sys.stdin.readline().rstrip())))
    
# deepcopy 사용
newMap = copy.deepcopy(m)

for x in range(r):
    for y in range(c):
        if m[x][y] == '.':
            continue
        
        # 상하좌우를 체크해주며, m[nx][ny] 가 지도 외 범위거나 바다라면 바다의 개수 cnt를 ++ 해준다.
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                cnt += 1
                continue
            elif m[nx][ny] == '.':
                cnt += 1
        if cnt >= 3:
            newMap[x][y] = '.'

# 여기까지 하면 전체 지도 크기는 동일하고, 섬이 침몰했는지 안했는지만 newMap 에 나타나게 된다.
# 이제 지도를 새로 그려주는 작업을 진행해보자.

# 새로 그릴 지도의 크기를 정해줄 변수들
startRow, endRow, startCol, endCol = 0, 0, 0, 0
minIndex, maxIndex = c-1, 0

# 앞에서부터 탐색
for i in range(r):
    if 'X' in newMap[i]:
        startRow = i
        break

# 뒤에서부터 탐색
for i in range(r-1, -1, -1):
    if 'X' in newMap[i]:
        endRow = i
        break
    
for i in range(startRow, endRow+1):
    temp = [i for i, value in enumerate(newMap[i]) if value == 'X']
    if not temp:
        continue
    minTemp = temp[0]
    maxTemp = temp[-1]
    minIndex = min(minIndex, minTemp)
    maxIndex = max(maxIndex, maxTemp)

for i in range(startRow, endRow+1):
    for j in range(minIndex, maxIndex+1):
        print(newMap[i][j], end="")
    print()