n = int(input())
list = list(map(int, input().split()))
'''
일찍 돈을 뽑는 사람이 앞에 있을 수록 시간이 단축된다.
1. 리스트 오름차순으로 정렬
2. 정렬된 리스트 for문 돌면서 출력하면 끝인듯?
3. 시간복잡도는 n?
'''

list.sort()
cnt = 0
sum = 0

for i in list:
    cnt += i
    sum += cnt
    
print(sum)