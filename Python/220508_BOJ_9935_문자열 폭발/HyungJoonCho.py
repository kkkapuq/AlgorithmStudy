from ntpath import join
import sys

# 일반 문자열 입력받기
str = list(sys.stdin.readline().strip())

# 폭발 문자열 입력받기
bombStr = list(sys.stdin.readline().strip())
tempStr = "".join(bombStr)

# 폭발 문자열 길이
bombLen = len(bombStr)

# 일반 문자열 넣을 스택
stack = []

# 잘못된 풀이
# 일반문자열 크기만큼 for문 돌면서, 폭발문자열과 같은 문자라면 pop해주기
# for i in str:
#     stack.append(i)
#     if i in bombStr:
#         stack.pop()

# if stack:
#     print("".join(stack))
# else:
#     print("FRULA")

# 일반문자열 크기만큼 for문 돌면서 스택 쌓아주기
for i in str:
    stack.append(i)
    if i == bombStr[-1]:
        if bombStr == (stack[-bombLen:]):
            del(stack[-bombLen:])

if stack:
    print("".join(stack))
else:
    print("FRULA")