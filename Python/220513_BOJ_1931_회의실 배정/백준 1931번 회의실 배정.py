confer_max = int(input())
confer_time = []
for _ in range(confer_max):
    confer_time.append(list(map(int, input().split())))
confer_time.sort()
confer_time.sort(key = lambda x: (x[1], x[0]))

ans = end = 0
for s, e in confer_time:
    if s >= end:
        ans += 1
        end = e
print(ans)