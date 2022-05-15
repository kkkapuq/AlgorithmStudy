import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = [[] for _ in range(n)]
answer = [[0] * n for _ in range(n)]

for idx in range(n):
    graph[idx].extend(list(map(int, input().rstrip().split())))

answer[0][0] = graph[0][0]
row = 0
col = 0
for row in range(1, n):
    for col in range(row + 1):
        if row >= 1 and col >= 1:
            answer[row][col] = max(answer[row - 1][col - 1], answer[row - 1][col]) + graph[row][col]
        elif col == 0:
            answer[row][col] = answer[row - 1][col] + graph[row][col]

print(max(answer[n-1]))
