def reverse(x: int):
    if x == 0:
        return 0
    
    tempStr = str(abs(x))
    answer = 0
    
    xList = list(tempStr)
    xList.reverse()
    
    while xList[0] == '0':
        del xList[0]
    
    if x < 0:
        answer = int('-' + ''.join(xList))
        if answer < -2**31:
            return 0
        return answer
    elif x > 0:
        answer = int(''.join(xList))
        if answer > 2**31-1:
            return 0
        return answer
    else:
        return 0
            
temp = '-021'
print(int(temp))