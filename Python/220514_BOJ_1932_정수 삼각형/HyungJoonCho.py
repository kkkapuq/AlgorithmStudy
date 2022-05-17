n = int(input())

# 숫자를 저장할 2차원 배열 만들기
v = []
for _ in range(n):
    v.append(list(map(int, input().split())))
    
# 0번째 인덱스와 v[i][j] 인덱스만 사용 가능, 이 두개만 써서 최대값 계산하기
for i in range(1, n):
    for j in range(len(v[i])):
        # 맨 왼쪽, 오른쪽 숫자는 자기랑 자기 위꺼 더하면됨
        if j == 0:
            v[i][j] = v[i][j] + v[i-1][j]
        elif j == len(v[i])-1:
            v[i][j] = v[i][j] + v[i-1][j-1]
        else:
            v[i][j] = max(v[i-1][j-1], v[i-1][j]) + v[i][j]

print(max(v[n-1]))