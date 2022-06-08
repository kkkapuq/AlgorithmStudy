'''
1. 입력받는 문자를 배열로 받는다.
2. i번째 문자가 다른 문자의 접두사인가? 를 판별하고, 맞다면 해당 문자는 제외시켜준다.
3. 다른거랑 다 비교를 했는데 접두사가 아니라면, cnt++ 해준다.
4. 알파벳 소문자로만 들어오니까, 알파벳순으로 정렬을 해주면 계산하기 쉬울 것 같다.
4-1. 그냥 정렬하면 첫번째 단어 기준으로해서 안됨
5. 접두사가 되는 단어는 다른 단어보다 같거나 짧으므로, 비교하고자 하는 단어가 다른 단어보다 길면 continue 해버리자
'''
'''
#틀린 풀이

import sys
n = int(input())
cnt = 0

wordList = []
for i in range(n):
    wordList.append(sys.stdin.readline().rstrip())

for i in range(n):
    flag = False
    for j in range(i+1, n):
        if len(wordList[i]) > len(wordList[j]):
            continue
        else:
            if wordList[i] == wordList[j][0:len(wordList[i])]:
                flag = True
                break
    if not flag:
        cnt += 1
        
print(cnt-1)
'''
import sys
n = int(input())
cnt = 0

wordList = []
for i in range(n):
    wordList.append(sys.stdin.readline().rstrip())

wordList.sort(key=len)

for i in range(n):
    flag = False
    for j in range(i+1, n):
        if wordList[i] == wordList[j][0:len(wordList[i])]:
            flag = True
            break
    if not flag:
        cnt += 1
        
print(cnt)