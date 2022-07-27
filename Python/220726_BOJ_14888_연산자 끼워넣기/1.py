'''
1. 모든 케이스를 돌면서 최대, 최소를 찾아야한다.
2. dfs/bfs 일거같은데......... 계산하다가 갖고있던 최대/최소보다 크거나 작으면 기존에 계산하던거 패스하고 다음껄로 넘어가야되니까 백트래킹?
'''
n = int(input())
numList = list(map(int, input().split()))
opAdd, opSub, opMul, opDiv = map(int, (input().split()))

visited = [False] * n
maxNum, minNum, temp = -1e9, 1e9, numList[0]

def dfs(i, add, sub, mul, div, tempSum):
    global maxNum, minNum
    if i == n:
        maxNum = max(maxNum, tempSum)
        minNum = min(minNum, tempSum)
        return
    
    if add > 0:
        dfs(i+1, add - 1, sub, mul, div, tempSum + numList[i])
    if sub > 0:
        dfs(i+1, add, sub - 1, mul, div, tempSum - numList[i])
    if mul > 0:
        dfs(i+1, add, sub, mul - 1, div, tempSum * numList[i])
    if div > 0:
        dfs(i+1, add, sub, mul, div - 1, int(tempSum / numList[i]))

dfs(1, opAdd, opSub, opMul, opDiv, temp)
print(maxNum)
print(minNum)

# import sys

# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //

# maximum = -1e9
# minimum = 1e9


# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return

#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


# dfs(1, num[0], op[0], op[1], op[2], op[3])
# print(maximum)
# print(minimum)
            
            