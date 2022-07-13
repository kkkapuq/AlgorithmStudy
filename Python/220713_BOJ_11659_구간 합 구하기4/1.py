'''
1. 그냥 풀면 시간초과 난다. 누적합으로 풀자
2. sumList에 1번째부터 n번째까지의 합을 넣어주고, 마지막엔 sumList[j] - sumList[i-1] 로 출력만해주면됨.
'''

n, m = map(int, input().split())

numList = list(map(int, input().split()))
sumList = [0]

tempSum = 0

for i in numList:
    tempSum += i
    sumList.append(tempSum)

for _ in range(m):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i-1])
