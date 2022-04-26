from sys import stdin

length, target = map(int, stdin.readline().split())

num_list = list(map(int, stdin.readline().split()))

s_idx = 0
e_idx = 0
total = num_list[s_idx]
answer = set()

while True:
    while total >= target and s_idx <= e_idx:
        answer.add(e_idx - s_idx + 1)
        total -= num_list[s_idx]
        s_idx += 1
    e_idx += 1
    if e_idx >= length:
        break
    total += num_list[e_idx]

print(0 if len(answer) == 0 else min(answer))
