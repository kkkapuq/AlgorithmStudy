from operator import truediv
import sys

INF = int(1e9)
input = sys.stdin.readline


def bellman_ford(start):
    cost = [INF] * (N + 1)
    cost[start] = 0
            
    for i in range(N):
        for s, e, c in edges:
            if cost[e] > cost[s] + c:
                cost[e] = cost[s] + c
                
                if i == N - 1:
                    return True
    return False

for _ in range(int(input())):
    
    edges = []
    
    N, M, W = map(int, input().split())
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        
        edges.append((a, b, c))
        edges.append((b, a, c))
        
    for _ in range(W):
        a, b, c = map(int, input().split())
        
        edges.append((a, b, -c))

    
    cycle = bellman_ford(1)

    if cycle:
        print("YES")
    else:
        print("NO")