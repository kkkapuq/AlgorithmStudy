from typing import List


def solution(alp, cop, problems:List):
    answer = 0
    # 사실 제일 높은 알고력과 코딩력만 맞추면 나머진 다 풀수있음
    maxAlp = 0
    maxCop = 0
    
    for alpReq, copReq, alpRwd, copRwd, cost in problems:
        maxAlp = max(maxAlp, alpReq)
        maxCop = max(maxCop, copReq)
    
    
    
    
    
    
    return answer

solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])