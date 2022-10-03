import re

def solution(registered_list, new_id):
    # ID 유효 검사 통과하면 1, 아니면 0
    flag = 0
    numberList = []
    maxNum = 0
    
    s = re.findall('[a-zA-Z]', new_id)
    n = re.findall('\d', new_id)
    
    answer = removeZero(new_id)
    
    if answer in registered_list and new_id in registered_list:
        s1 = re.findall('[a-zA-Z]', answer)
        n1 = re.findall('\d', answer)
        maxNum = 0
        
        # 최대값 찾기
        for index, i in enumerate(registered_list):
            ss1 = re.findall('[a-zA-Z]', i)
            nn1 = re.findall('\d', i)
            
            if ss1 == s1:
                if not nn1:
                    numberList.append(0)
                    continue
                else:
                    nn1 = ''.join(nn1)
                    nn1 = int(nn1)
                    numberList.append(nn1)
                
                    
        n1 = ''.join(n1)
        n1 = int(n1)
        
        if len(numberList) > 1:
            numberList.sort()
            for i in range(1, len(numberList)):
                if numberList[i] - numberList[i-1] > 1:
                    maxNum = numberList[i-1] + 1
                    flag = 1
        
        if flag == 1:
            n1 = maxNum
        else:
            n1 = max(numberList) + 1
        
        answer = ''.join(s1) + str(n1)
    
    else:
        return new_id
    
    return answer

def removeZero(newId):
    s = re.findall('[a-zA-Z]', newId)
    n = re.findall('\d', newId)
    
    if not n:
        n = ['1']

    while n[0] == '0' and len(n) > 1:
        del n[0]
    
    return ''.join(s+n)
    

solution(['bird99','bird98','bird101'], 'bird98')