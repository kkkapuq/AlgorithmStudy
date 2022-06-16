'''
1. 
'''

from collections import deque
import sys

sys.setrecursionlimit(10000)

answer = 0

def dfs(numLen, i, result, numbers, target):
    if i == numLen:
        if result == target:
            global answer
            answer += 1
        return
    dfs(numLen, i + 1, result + numbers[i], numbers, target)
    dfs(numLen, i + 1, result - numbers[i], numbers, target)


def solution(numbers, target):
    global answer
    
    numLen = len(numbers)
    dfs(numLen, 0, 0, numbers, target)
    
    return answer

solution([1, 1, 1, 1, 1,], 3)