n = int(input())

# 2차원 리스트 생성
room = [ [] for _ in range(n)]

# 시간 넣어주기
for i in range(n):
    temp = []
    x, y = map(int, input().split())
    temp.append(x)
    temp.append(y)
    room[i] = temp

# 시간 정렬
room.sort()
# print(room)
# 동시에 쓸수있는 회의실의 최대 수
max = 1
for i in range(n - 2):
    cnt = 1
    for j in range(i + 1, n - 1):
        x = room[i][0]
        y = room[i][1]
        nx = room[j][0]
        ny = room[j][1]
    
        # 다음 회의시간의 시작시간이 현재 진행중인 회의 시간 사이라면
        if nx < (ny - x):
            continue
        else:
            cnt += 1
    if max < cnt:
        max = cnt

print(max)