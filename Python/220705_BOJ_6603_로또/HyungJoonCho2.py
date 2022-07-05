'''
1. combinations을 쓰지 않는 풀이
2. 백트래킹으로 풀어보자. dfs로 풀거니까 스택으로 풀거임
3. dfs함수 내의 answerList 에 stack for문을 돌면서 넣어준다.
4. answerList의 크기가 6이 된다면 return 해줘서 재귀 그만돌게해주기
5. stack을 돌면서, answerList에 더해주는데, 사이즈가 6 미만이라면 
'''

import sys

def dfs():
    
    # answerList 의 길이가 6이면 출력해주고 return
    if len(answerList) == 6:
        print(" ".join(map(str, answerList)))
        return
    
    # answerList 비어있으면 스택 들어온거 바로 넣어주기
    if len(answerList) == 0:
        for i in lottoList:
            answerList.append(i)
            dfs()
            answerList.pop()
        return
    
    # 스택 돌면서 answerList에 쌓아주기, 직전 수보다 i가 크다면 append 해준다.
    # 만약 i가 직전 수보다 작다면 pop해줌
    for i in lottoList:
        if i > answerList[len(answerList) - 1]:
            answerList.append(i)
            dfs()
            answerList.pop()

while True:
    
    lottoList = list(map(int, sys.stdin.readline().split()))
    
    k = lottoList[0]
    if k == 0:
        break
    del lottoList[0]
    
    answerList = []
    
    dfs()
    print()
