import sys
input = sys.stdin.readline

n = int(input().rstrip())

timetable = []

for _ in range(n):
    s, e = map(int, input().rstrip().split())
    timetable.append((s, e))

timetable.sort(key=lambda x: x[0], reverse=True)
timetable.sort(key=lambda x: x[1], reverse=True)

conference = timetable.pop()
total = 1
e = conference[1]
while timetable:
    conference = timetable.pop()
    s = conference[0]
    if s >= e:
        total += 1
        e = conference[1]
print(total)

