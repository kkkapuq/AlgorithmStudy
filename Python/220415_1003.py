# 3까지는 문제를 통해서 유추 가능하므로 3까지 하드코딩
cntZero = [1, 0, 1]
cntOne = [0, 1, 1]

def fibonacci(n):
    #2번 index까지는 그냥 노출
    length = len(cntZero)
    if n >= length:
        for i in range(length, n + 1):
            cntZero.append(cntZero[i-2] + cntZero[i-1])
            cntOne.append(cntOne[i-2] + cntOne[i-1])
    print(cntZero[n], cntOne[n])
        
#T번 입력하는거 입력받기
T = int(input())

#T번 반복한다
for i in range(T):
    n = int(input())
    fibonacci(n)