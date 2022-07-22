'''
1. N = 일의 개수, T = 시간, S = 끝내야 하는 시간
2. 하루 24시간인 daytime을 놓고, s가 낮은 순서로 정렬.
'''

n = int(input())
daytime = 24
taskList = []
timeSum = 0
curTime = 0
startTime = 0
maxFlag = 1

for i in range(n):
    ts = list(map(int, input().split()))
    taskList.append(ts)
    
# key (s) 에 따른 오름차순 정렬, (먼저 끝내야 하는 일 순으로 정렬)
taskList.sort(key=lambda x:x[1])

 # 0시부터 23시 시작까지, 주어진 시간 안에 일을 처리하지 못할 때까지 + 해주고, 처리하지 못하는 시간이 되면 현재값(i) - 1 해준다.
for i in range(daytime):
    curTime = i
    for j in taskList:
        curTime += j[0]
        if curTime > j[1]:
            maxFlag = 0
            break
    if maxFlag == 0:
        startTime = i-1
        break
print(startTime)