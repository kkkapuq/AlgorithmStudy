import sys
from collections import deque

a, b = map(int, input().split())

# bfs(Breadth-first-Search) 너비우선 탐색 사용
max = 100000
que = deque([a])
queList = [0] * max
def bfs():
    while(que):
        val = que.popleft()
        # print(val , queList[val])
        if val == b:
            return(queList[val])
        for c in (val-1, val+1, val*2):
            if 0 <= c <= max and not queList[c]:
                queList[c] = queList[val] + 1
                que.append(c)
print(bfs())

# 곱할때 더할때 뺄때의 경우를 나누어 생각해봄
# count = 0
# f_flag = False
# m_flag = False
#
# while a != b:
#     # 곱할때
#     if 2 * a <= b:
#         a = 2 * a
#         count += 1
#         f_flag = True
#
#     # 더할때
#     elif a < b <= 1.5 * a:
#         if f_flag == True:
#             while a + 2 < b:
#                 a += 2
#                 count += 1
#
#         while a < b:
#             a += 1
#             count += 1
#
#     # 뺄 때
#     elif 1.5 * a < b < 2 * a:
#         while
#         a -= 1
#         count += 1
#         m_flag = True
#
#     elif b < a:
#         a -= 1
#         count += 1
#
#     print(f"{a} : {count}")
# print(count)

