# import sys

# 시간초과 풀이
# n, m = map(int, input().split())

# hPeople = [ sys.stdin.readline().rstrip() for _ in range(n) ]
# sPeople = [ sys.stdin.readline().rstrip() for _ in range(m) ]

# answer = []
# for i in hPeople:
#     if i in sPeople:
#         answer.append(i)

# for i in sPeople:
#     if i in hPeople:
#         if i in answer:
#             continue
#         else:
#             answer.append(i)
        
# print(len(answer))
# print('\n'.join(answer))

import sys

n, m = map(int, input().split())

hPeople = [ sys.stdin.readline().rstrip() for _ in range(n) ]
sPeople = [ sys.stdin.readline().rstrip() for _ in range(m) ]

answer = list(set(hPeople) & set(sPeople))
answer.sort()

print(len(answer))
print('\n'.join(answer))