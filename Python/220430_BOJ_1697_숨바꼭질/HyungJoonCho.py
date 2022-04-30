import sys
from collections import deque

def bfs(x):
    queue = deque([x])
    while queue:
        #현재 위치에서 동생(k)를 만났다면 거리 return
        x = queue.popleft()
        if x == k:
            return dist[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[x]+1
                queue.append(i)

n, k = map(int, input().split())
MAX = 100000 #거리 제한
dist = [0] * (MAX + 1)
print(bfs(n))