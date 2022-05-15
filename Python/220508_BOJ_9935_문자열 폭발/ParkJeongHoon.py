import sys
from collections import deque

NO_CHAR = "FRULA"
input = sys.stdin.readline

string = input().rstrip()
explode = input().rstrip()

stack = []
e_len = len(explode)

for char in string:
    stack.append(char)
    if char == explode[-1] and "".join(stack[-e_len:]) == explode:
        del stack[-e_len:]

answer = "".join(stack)

print(NO_CHAR if answer == "" else answer)
