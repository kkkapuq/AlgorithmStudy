'''
1. 예제별 공식 만들어보자.
1번 예제
1째줄 - 0, 4, 8, 12 -> str[n-n], str[n+1], str[n+5], str[n+9] -> 4씩 증가
2째줄 - 1, 3, 5, 7, 9, 11, 13 -> str[n-2], str[n], str[n+2], str[n+4] ... str[n+10] -> 2씩 증가
3째줄 - 2, 6, 10 -> str[n-1], str[n+3], str[n+7] -> 4씩 증가

2번 예제
1째줄 - 0, 7, 13 -> str[n-n], str[n+3], str[n+9] -> 이거 아닌듯


'''
def convert(s: str, numRows: int):
    if numRows == 1:
        return s
    
    strArr = [''] * numRows
    strIndex = 1
    flag = 1
    
    for i in s:
        strArr[strIndex-1] += i
        if strIndex == numRows:
            flag = 0
        elif strIndex == 1:
            flag = 1
        
        if flag == 1:
            strIndex += 1
        else:
            strIndex -= 1
    
    return print(''.join(strArr))
        

convert('PAYPALISHIRING', 3)