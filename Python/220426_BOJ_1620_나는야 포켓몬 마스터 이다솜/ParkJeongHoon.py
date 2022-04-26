from sys import stdin
input = stdin.readline

total, cnt = map(int, input().split())

poketmon_list = list()
poketmon_list.append(0)
poketmon_dict = dict()
for idx in range(1, total + 1):
    poketmon = input().strip()
    poketmon_list.append(poketmon)
    poketmon_dict[poketmon] = idx

for _ in range(cnt):
    question = input().strip()
    if question.isdigit():
        answer = poketmon_list[int(question)]
    else:
        answer = poketmon_dict[question]
    print(answer)
