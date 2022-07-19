'''
1. N = 일의 개수, T = 시간, S = 끝내야 하는 시간
2. 하루 24시간인 daytime을 놓고, s가 낮은 순서로 정렬.
'''

n = int(input())
taskList = []
startTime = float('inf')

for i in range(n):
    ts = list(map(int, input().split()))
    taskList.append(ts)
    
# key (s) 에 따른 오름차순 정렬, (먼저 끝내야 하는 일 순으로 정렬)
taskList.sort(key=lambda x:x[1])

for i in range(len(taskList)):
    curTime = taskList[i][0]
    for j in range(i):
        curTime += taskList[j][0]
    if taskList[i][1] < curTime:
        print(-1)
        exit()
    else:
        startTime = min(startTime, taskList[i][1]-curTime)
            
print(startTime)