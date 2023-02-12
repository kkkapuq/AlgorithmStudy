from collections import deque

def solution(queue):
    answer = [0, 0, 0]
    
    '''
    1. 최소 2번은 넣어야 1, 2, 3의 갯수가 같아짐
    2. 맵이랑 딕셔너리 ㄱㄱ
    3. queue 길이를 3등분 하면 1, 2, 3의 갯수가 같아짐
    '''
    
    # queue 에 있는 1, 2, 3의 개수 dict에 넣어주기
    numberDict = {1: 0, 2: 0, 3: 0}
    for i in queue:
        numberDict[i] += 1
        
    q = deque(queue)
    n = len(queue) // 3
    while True:
        if numberDict[1] == numberDict[2] == numberDict[3]:
            break
        
        temp = q.popleft()
        numberDict[temp] -= 1
        
        if numberDict[1] < n:
            q.append(1)
            numberDict[1] += 1
            answer[0] += 1
        elif numberDict[2] < n:
            q.append(2)
            numberDict[2] += 1
            answer[1] += 1
        elif numberDict[3] < n:
            q.append(3)
            numberDict[3] += 1
            answer[2] += 1
    
    return answer

print(solution([2,1,3,1,2,1]))