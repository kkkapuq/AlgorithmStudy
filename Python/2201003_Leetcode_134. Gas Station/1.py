from collections import deque

def canCompleteCircuit(gas: list[int], cost: list[int]):
    
    '''
    시간초과 풀이...
    # 한바퀴 만큼 순회
    n = len(gas)
    
    if n == 1:
        if gas[0] >= cost[0]:
            return 0
        else:
            -1
    
    for i in range(n):
        if gas[i] > cost[i]:
            remainGas = gas[i]
            for j in range(i, n+i):
                # 끝 인덱스에서 처음인덱스로 가서 계산해야함
                # 4 ~ 9 면 인덱스는 4~8까지 실행
                # ex) i = 4, j = 4, index = 0 ...
                # ex) i = 4, j = 5, index = 1 ...
                # ex) i = 4, j = 8, index = 4 ...
                
                # j가 n보다 클때
                if j >= n:
                    remainGas -= cost[j-n]
                    if remainGas >= 0:
                        remainGas += gas[j-n+1]
                
                # j가 마지막 인덱스에서 처음 인덱스로 갈 때
                elif j == n-1:
                    remainGas -= cost[j]
                    if remainGas >= 0:
                        remainGas += gas[0]
                
                # 처음과 끝 사이에서 움직일 때
                else:
                    remainGas -= cost[j]
                    if remainGas >= 0:
                        remainGas += gas[j+1]
            if remainGas > 0:
                return i
    return -1 
    '''
    
    # trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
    # for i in range(n):
    #     trip_tank += gas[i] - cost[i]
    #     curr_tank += gas[i] - cost[i]
    #     if curr_tank < 0:
    #         start = i + 1
    #         curr_tank = 0 
    # return start if trip_tank >= 0 else -1
    
    # 1바퀴 돌만큼의 기름이 없는경우엔 -1 리턴
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점이 안 되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start
    


canCompleteCircuit([1,2,3,4,5], [3,4,5,1,9])