'''
1. r, c = 행렬, n = 시간
2. 유기농 배추랑 유사한 문제같음. dfs로 상하좌우 탐색해주자.
3. 케이스는 n이 3가지인 케이스로 나뉜다.
    1) 짝수일때 - 0으로 도배한 graph return
    2) numList 안에 있는 수일 때 - 초기 폭탄 터진 모양, numList는 초항 3, 공차가 4인 등차수열
    3) 그 외일 때 - 0으로 도배한 뒤에 터진 폭탄 터진 모양
'''
import sys
    
# 문제에 필요한 정보 입력
r, c, n = map(int, input().split())

# 초기상태의 그래프, 폭파된 상태의 그래프
graph = []
bombedGraph = []
bombedGraph2 = []

# 동서남북 탐색 리스트
nxny = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 초항 3, 공차 4인 등차수열
numList = list(range(3, n+1, 4))

# 0으로 채운 그래프
allBombGraph = [ ['O' for i in range(c)] for j in range(r) ]
tempGraph = [['O']*c for i in range(r)]
print(allBombGraph)
print(tempGraph)

# r x c의 행렬 만들기
for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

# n이 1이하일땐 초기 상태 노출
if n<=1 :
    for i in graph:
        print("".join(map(str, i)))

# n이 짝수일 때 모두 폭탄으로 채운 행렬 return
elif n % 2 == 0:
    for i in allBombGraph:
        print("".join(map(str, i)))
    
else:
    # # 첫번째 폭탄이 폭발한 경우
    # bombedGraph = allBombGraph
    # for i in range(r):
    #     for j in range(c):
    #         if graph[i][j] == 'O':
    #             bombedGraph[i][j] = '.'
    #         else:
    #             for k, l in nxny:
    #                 if i+k >= 0 and i+k < r and j+l < c and graph[i+k][j+l] == 'O':
    #                     bombedGraph[i][j] = '.'
    #                     break
    
    bombs1 = [['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if graph[y][x]=='O': bombs1[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and graph[y+i][x+j]=='O':
                        bombs1[y][x] = '.'
                        break
    
    # # 두번째 폭탄이 폭발한 상태
    # bombedGraph2 = allBombGraph
    # for i in range(r):
    #     for j in range(c):
    #         if bombedGraph[i][j] == 'O':
    #             bombedGraph2[i][j] = '.'
    #         else:
    #             for k, l in nxny:
    #                 if i+k >= 0 and i+k < r and j+l < c and bombedGraph[i+k][j+l] == 'O':
    #                     bombedGraph2[i][j] = '.'
    #                     break
    
    # 두번째 폭탄이 터진 상태
    bombs2 = [['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if bombs1[y][x]=='O' : bombs2[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and bombs1[y+i][x+j]=='O':
                        bombs2[y][x] = '.'
                        break
                    
    if n%4 == 3:
        for i in bombedGraph:
            print("".join(map(str, i)))
            
    if n%4 == 1:
        for i in bombedGraph2:
            print("".join(map(str, i)))