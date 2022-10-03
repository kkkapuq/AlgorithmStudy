def solution(k):
    answer = 0
    
    matchesList = {
        '0' : 6, 
        '1' : 2, 
        '2' : 5, 
        '3' : 5, 
        '4' : 4, 
        '5' : 5, 
        '6' : 6, 
        '7' : 3, 
        '8' : 7, 
        '9' : 6
    }
    
    wordList = []
    word = ''
    while k == 0:
        for i in range(9):
            value = matchesList[str(i)]
            if value <= k:
                word += str(i)
                k -= value
        
            
    
    return answer