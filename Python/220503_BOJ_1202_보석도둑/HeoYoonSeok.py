import sys
from heapq import heappop, heappush
N, K = map(int, input().split())
input = sys.stdin.readline
answer = 0
jewelLst, bagLst= [0] * N, [0] * K
for i in range(N):
    jewelLst[i] = list(map(int, sys.stdin.readline().split()))
jewelLst = sorted(jewelLst, reverse = True)

for i in range(K):
    bagLst[i] = int(sys.stdin.readline())
bagLst = sorted(bagLst)

q = []

for bag in bagLst:
    while jewelLst and bag >= jewelLst[-1][0]:
        heappush(q, -jewelLst.pop()[1])
    if q:
        answer -= heappop(q)

print(answer)