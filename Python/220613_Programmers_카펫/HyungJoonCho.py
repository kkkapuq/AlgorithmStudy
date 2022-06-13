'''
a는 가로, b는 세로, 정답은 [a, b] 형태로
1. a >= b
2. ab = carpet (brown + yellow)
3. yellow = ab -2a -2b + 4
4. brown = (a*b) - {(a-2) * (b-2)} = ab - ab + 2a + 2b - 4 = 2a + 2b - 4 = ab - yellow

'''

def solution(brown, yellow):
    answer = []
    
    carpet = brown + yellow # carpet = a * b
    
    for b in range(1, carpet+1):
        if (carpet % b) == 0:
            a = carpet / b # 가로는 전체 / 세로
            if a >= b: # 만약 가로 >= 세로라면 식으로 도출
                if (a*b) - (2*a) -(2*b) + 4 == yellow:
                    answer.append(a)
                    answer.append(b)
    
    return answer

solution(8, 1)