# 숫자는 답 표현식에 표현
# 쟁반은 스택이다.
# 연산자는 쟁반에 쌓아두다가 쟁반에 쌓은 것보다 우선순위가 낮은 것이 오면
# 쟁반에 있는 것들 중 우선순위가 높은 것들만 순서대로 빼서 표현식에 넣는다.

import sys
from collections import deque

input = sys.stdin.readline

answer = ""
operator = deque()

expression = input().rstrip()

for temp in expression:
    if temp.isalpha():
        answer += temp
    else:
        if temp == "(":
            operator.append(temp)
        elif temp == ")":
            length = len(operator)
            while operator[length - 1] != "(":
                answer += operator.pop()
                length -= 1
            operator.pop()
        elif temp == "*" or temp == "/":
            length = len(operator)
            if length != 0 and operator[length - 1] != "+" and operator[length - 1] != "-":
                while length > 0 and (operator[length - 1] == "*" or operator[length - 1] == "/"):
                    answer += operator.pop()
                    length -= 1
            operator.append(temp)
        else:
            length = len(operator)
            while length > 0 and operator[length - 1] != "(":
                answer += operator.pop()
                length -= 1
            operator.append(temp)
length = len(operator)
while length > 0:
    answer += operator.pop()
    length -= 1

print(answer)
