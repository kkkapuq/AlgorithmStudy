n, m = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
lst = [list(map(int, list(input()))) for i in range(m)]
visit = [[0] * n for i in range(m)]

print(lst)
print(visit)