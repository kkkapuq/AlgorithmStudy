'''
# 이코테_그리디_실전문제2_큰 수의 법칙
# 난이도 - 하
# 제한시간 - 30분

1. M번 더해서 가장 큰 수를 만들기
2. K번을 초과해서 연속으로 더해질 수는 없음

'''
'''
# 내 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
sec = data[-2]

# K + 1만큼 길이를 가진 수열이 M // K+1 만큼 반복되고, 이후 M % K+1 만큼의 수열의 인덱스까지 더해준다. (나누어 떨어지지 않을 수 있으니)
sumList = []
for i in range(k):
    sumList.append(first)
sumList.append(sec)

# 이렇게 하면 하나의 수열인 sumList가 완성된다. 이후에 위 조건대로 출력해주면 끝.
result = 0
# 수열을 더한 값들(sum(sumList))이 M // K+1 만큼 더해지니, 다음과 같이 곱해주기
result += sum(sumList) * (m // (k+1))
# 나머지(m%(k+1)) 값의 인덱스만큼 더해주기
result += sum(sumList[:m%(k+1)])
print(result)

'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
sec = data[-2]

# ex) k가 3이라면, first를 3번 더한것에 + 1 한게 수열의 길이가 된다.
# 5 8 3이 들어왔다고 가정하면 (8 + 8 + 8 + 5) 이렇게 한쌍이 되는거임
length = k + 1

# 그렇다면 m // k만큼 가장 큰 수가 더해질 것이고, m // k 하고 남은 m % (k+1) 만큼 더 더해주면 된다.
# 예를들어 5 10 3 이 들어왔다면 (8 + 8 + 8 + 5) + (8 + 8 + 8 + 5) + (8 + 8) 이렇게 되는 것이다.
# m // k만큼 가장 큰 수가 나온다
count = (m // length) * k
# m / (k+1)이 나누어 떨어지지 않는다면, m % (k+1) 만큼 가장 큰수를 더 더해준다.
count += m % length

# 결과 출력
result = count * first
# 전체 갯수 m에서 큰 수가 나온만큼인 count를 빼주면 나머지는 두번째로 큰 수의 개수가 된다.
result += (m-count) * sec
print(result)

