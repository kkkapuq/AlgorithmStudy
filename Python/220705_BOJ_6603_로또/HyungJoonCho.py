from itertools import combinations
import sys

'''
1. combinations 쓰면 될거같은데..?
'''

while True:
    
    lottoList = list(map(int, sys.stdin.readline().split()))
    
    k = lottoList[0]
    if k == 0:
        break
    del lottoList[0]
    
    answerList = list(combinations(lottoList, 6))
    answerList.sort()
    
    for i in answerList:
        print(" ".join(map(str, i)))
    
    print()

