import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

edges = []

cost = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())

    edges.append((a, b, c))

def bellman_ford(start):

    cost[start] = 0

    for i in range(v):
        for j in range(e):

            start = edges[j][0]
            end = edges[j][1]
            c = edges[j][2]

            if cost[start] != INF and cost[end] > cost[start] + c:
                cost[end] = cost[start] + c

                if i == v - 1:
                    return True

    return False

cycle = bellman_ford(1)

if cycle:
    print("-1")
else:
    for i in range(2, v + 1):
        if cost[i] == INF:
            print("-1")
        else:
            print(cost[i])