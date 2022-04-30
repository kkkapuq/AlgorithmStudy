import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
answer = 0

def find(x):
	if x == parent[x]:
		return x
	y = find(parent[x])
	parent[x] = y
	return y

def union(x, y):
	x = find(x)
	y = find(y)
	
	if x > y:
		parent[x] = y
	else:
		parent[y] = x
		
h = []


for _ in range(E):
	s, e, v = map(int, input().split())
	heapq.heappush(h, (v, s, e))
	
while h:
	v, s, e = heapq.heappop(h)
	x, y = find(s), find(e)
	
	if x == y:
		continue
	else:
		answer += v
		union(s, e)
		
print(answer)