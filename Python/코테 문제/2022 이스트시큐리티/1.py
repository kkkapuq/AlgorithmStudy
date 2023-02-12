


def solution(histogram):
    answer = 1
    
    # 막대그래프의 가로
    width = len(histogram[0])
    # 막대그래프의 최대 높이
    height = len(histogram)
    
    # 경우의 수 리스트
    tempList = []
    '''
    1. 2일 때만 경우의수 체크해주면 됨
    2. 1일 때는 break 해서 쌓인 경우의 수 곱해주면 됨
    3. 위에서부터 체크하는걸로 ㄱㄱ
    '''
    for i in range(width):
        cnt = 0
        for j in range(height):
            if histogram[j][i] == 0 and cnt == 0:
                continue
            if histogram[j][i] == 0:
                cnt = 0
            elif histogram[j][i] == 1:
                break
            elif histogram[j][i] == 2:
                cnt += 1
                
        tempList.append(cnt)
    
    for i in tempList:
        answer *= i+1
    
    return answer


param = [[0,0,0,0,0,0,1],
         [0,0,0,1,0,0,1],
         [0,1,0,1,0,0,1],
         [1,1,2,2,1,0,1],
         [2,2,2,2,1,2,2],
         [2,2,1,1,1,2,2],
         [2,2,1,1,1,2,2]]
print(solution(param))