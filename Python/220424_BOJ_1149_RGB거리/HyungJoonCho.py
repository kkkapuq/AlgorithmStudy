'''
1. 1번집은 2번집과 색이 같지 않아야 한다고 명시되있으므로, 1과 2는 하드코딩 해도 괜찮을듯?
2. 일단 최소값을 골라보고, n까지의 최소값들의 합이 최소인걸로 바꿔주면서 for문 돌려줘보자..
3. 근데 i-1, i, i+1 의 색의 집이 달라야 한다는건 곧 i-2, i-1, i 의 색이 달라야한다는거아님?
----------------------------------
1. 위 방식대로 하면.. 전체적인 비용의 최소값을 구하는건 에러가 발생할 것 같다.
2. house[i][0] 은 규칙에 맞게 1~i까지 칠했을 때 i번이 빨강인 케이스 중 가장 작은 값을 나타낸다.
3. 같은 방식으로 house[i][1] 과 house[i][2]를 구해주면 된다. 그리고 마지막까지 다 더해졌다면..
4. 빨강, 초록, 파랑으로 칠했을 때 각 케이스별 비용을 모두 모아놓은 집합이다. 따라서 여기서 최소값을 구해주면 끝

'''
import sys
n = int(input())

house = []
for i in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    #빨강
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    #초록
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    #파랑
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]
    
print(min(house[-1]))