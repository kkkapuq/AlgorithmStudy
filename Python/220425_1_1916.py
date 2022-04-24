import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start_cost,start_node):
    dist = [ INF for _ in range(n+1)]
    dist[start_node] = 0
    q = [(start_cost,start_node)]

    while q:
        print(dist)
        p = heapq.heappop(q)
        cur_cost, cur_node = p[0], p[1]
        for next_cost, next_node in graph[cur_node]:
            if dist[next_node] > cur_cost + next_cost:
                dist[next_node] = cur_cost + next_cost
                heapq.heappush(q, (dist[next_node],next_node))
    return dist

# 도시 개수 n, 버스 개수 m
n = int(input().rstrip())
m = int(input().rstrip())

graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    start,end,cost = map(int,input().rstrip().rsplit())
    graph[start].append((cost,end))

want1, want2 = map(int,input().rstrip().rsplit())
answer = dijkstra(0,want1)
print(answer[want2])