
def letterCombinations(digits: str):
    
    if len(digits) < 1:
        return []
    
    phoneNum = [
        [],
        [],
        ['a','b','c'],
        ['d','e','f'],
        ['g','h','i'],
        ['j','k','l'],
        ['m','n','o'],
        ['p','q','r','s'],
        ['t','u','v'],
        ['w','x','y','z']
    ]
    
    '''
    23: ad ae af bd be bf cd ce cf // phoneNum[i] 를 len(phoneNum[i]) 만큼 append 해줌 
    234: adg adh adi aeg aeh aei afg afh afi // 2, 3, 4, len(phoneNum[2]) * len(phoneNum[3]) * len(phoneNum[4]) 만큼 phoneNum[2][0]을 append 해줌, 27
    237: adp adq adr ads aep aeq aer aes afp afq afr afs
         bdp bdq bdr bds bep beq ber bes bfp bfq bfr bfs
         cdp cdq cdr ...                        // len(phoneNum[2]) * len(phoneNum[3]) * len(phoneNum[7]) 만큼 phoneNume[2][i] 를 append, 36 수식은 맞는게 증명됨
    2347: adgp adgq adgr adgs adhp adhq adhr adhs adip adiq adir adis
          aegp aegq aegr aegs aehp aehq aehr aehs aeip aeiq aeir aeis
          .. // a가 생기는 수는 36개, len(phonNum[3]) * len(phonNum[4]) * len(phoneNum[7])
    
    '''
    
    answer = []
    answerSize = 1
    
    for i in digits:
        answerSize *= len(phoneNum[int(i)])
    
    tempList = []
    for i in digits:
        tempList.append(int(i))
        
    for i, number in enumerate(tempList):
        for j in phoneNum[number]:
            for k in range(i+1, len(tempList)):
                answer.append(j)
    
    print(answer)
    
letterCombinations('23')