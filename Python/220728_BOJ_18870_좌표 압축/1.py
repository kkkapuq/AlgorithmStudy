'''
1. 좌표압축 = 작은순서부터 인덱싱 해주는것
2. 입력된 좌표 리스트를 정렬해준다음... 순서대로 딕셔너리에 넣어주면 될듯?
'''
n = int(input())

numList = list(map(int, input().split()))

# set으로 중복 제거 및 정렬
setList = list(set(numList))
setList.sort()
answerDic = {}

for i in range(len(setList)):
    answerDic[setList[i]] = i

for i in range(len(numList)):
    print(answerDic[numList[i]], end=' ') 