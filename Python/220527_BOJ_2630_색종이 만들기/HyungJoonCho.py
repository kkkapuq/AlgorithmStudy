import sys

n = int(input())

# 2차원 리스트 생성
Mat = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

white,blue=0,0


def Color(x,y,n):
    global white,blue     
    check=Mat[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=Mat[i][j]:     #나머지 사각형의 색깔과 일치하지 않는다면 실행합니다.
                Color(x,y,n//2)            #1사분면
                Color(x,y+n//2,n//2)       #2사분면
                Color(x+n//2,y,n//2)       #3사분면
                Color(x+n//2,y+n//2,n//2)  #4사분면
                return

    if check==0:
        white+=1
        return
    else:
        blue+=1
        return

Color(0,0,n)
print(white)
print(blue)

