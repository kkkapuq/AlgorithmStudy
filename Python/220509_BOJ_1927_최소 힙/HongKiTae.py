from queue import PriorityQueue

nNum = int(input())
que = PriorityQueue(maxsize=nNum)
for _ in range(0, nNum):
    val = input()

    if val == '0':
        if que.empty():
            print('0')
        else:
            print(que.get())
    else:
        que.put(int(val))
