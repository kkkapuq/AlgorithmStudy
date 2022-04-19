from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()
print(queue)