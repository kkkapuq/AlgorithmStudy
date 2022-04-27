import sys

n = int(sys.stdin.readline())
house = []
for i in range(n):
    house.append(list(map(int, input().split())))
    
for i in range(1, n):
    #빨강
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    #파랑
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    #초록
    house[i][2] = min(house[i-1][1], house[i-1][0]) + house[i][2]

print(min(house[n-1][0], house[n-1][1], house[n-1][2]))