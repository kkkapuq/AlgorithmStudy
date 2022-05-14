
pyramid = []
pyramid_size = int(input())
answer = 0
for _ in range(pyramid_size):
    pyramid.append(list(map(int, input().split())))

############################### 시간 초과
# print(pyramid)
def bfs(layer, loc, val):
    global answer

    if layer == pyramid_size:
        if answer < val:
            answer = val
            # print(answer)
    else:
        for i in range(loc, loc + 2):
            # print(f"{layer}  {loc}  {val}  {i}")
            new_val = val + pyramid[layer][i]
            bfs(layer + 1, i, new_val)

# bfs(1, 0, pyramid[0][0])
# print(answer)
################################

# 피라미드 내려가면서 그냥 더해버리고 비교
for i in range(1,pyramid_size):
  for j in range(len(pyramid[i])):
    if j == 0:
      pyramid[i][j] = pyramid[i][j] + pyramid[i-1][j]
    elif j == len(pyramid[i])-1:
      pyramid[i][j] = pyramid[i][j] + pyramid[i-1][j-1]
    else:
      pyramid[i][j] = max(pyramid[i-1][j-1], pyramid[i-1][j]) + pyramid[i][j]

    print(f"{i} {j} {pyramid[i][j]}")
print(max(pyramid[pyramid_size - 1]))
