'''
1. 처음 마이너스부터 다음 마이너스가 오기 전까지 + 는 모두 더해줘야 최소값이 나온다.
2. 따라서, -를 기준으로 시작괄호를 열고, 다음 -가 나온다면 그때 괄호를 닫아주자.
'''


string = input()
sliceList = list(string.split('-'))

totalList = []
totalSum = 0

# -로 구분한 문자열 리스트를 for문 돈다.
for i in sliceList:
    # +가 있는 문자열이라면 +로 split 해준다, split된 plustList는 모두 더해져 totalList에 더해진다.
    if '+' in i:
        plusList = list(map(int, i.split('+')))
        sum = sum(plusList)
        totalList.append(sum)
    # +가 없는 문자열이라면 그냥 totalLIst에 더해준다.
    else:
        totalList.append(int(i))

# totalList의 0번 인덱스를 totalSum으로 세팅, 나머지는 다 빼준다.
for i in range(len(totalList)):
    if i == 0:
        totalSum = totalList[i]
    else:
        totalSum -= totalList[i]

print(totalSum)