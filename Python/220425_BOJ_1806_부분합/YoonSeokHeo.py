import sys
 
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
lst = list(map(int, input().split()))
 
answer = 1000000
length = 1
s, e = 0, 0
sum_num = lst[0]
 
while True:
	if sum_num >= m:
		answer = min(answer, length)
		sum_num -= lst[s]
		length -= 1
		s += 1
	else:
		e += 1
		length += 1
		if e == n:
			break
		sum_num += lst[e]
 
print(0 if answer == 1000000 else answer)