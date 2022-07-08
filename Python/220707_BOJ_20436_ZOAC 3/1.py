'''
1. 한글 자/모음별로 왼손, 오른손을 구분하니, 입력받은 문자열을 왼손으로 입력할지 오른손으로 입력할지 구분하는 작업 필요
2. 문자열을 돌면서 거리를 계산해주고, 거리만큼 time에 더해주면된다.
'''
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
ja = ['qwertasdfgzxcv']
mo = 'yuiophjklbnm'

sl, sr = input().split()
string = list(input())

lx, ly, rx, ry = None, None, None, None

# 초기 입력값의 좌표 구하기
for i in range(len(keyboard)):
    if sl in keyboard[i]:
        lx = i
        ly = keyboard[i].index(sl)
    
    if sr in keyboard[i]:
        rx = i
        ry = keyboard[i].index(sr)
            
time = 0

# 문자열 돌면서 거리 계산해주기
for i in string:
    time += 1
    if i in mo:
        for j in range(len(keyboard)):
            if i in keyboard[j]:
                nx = j
                ny = keyboard[j].index(i)
                
                time += abs(nx - rx) + abs(ny - ry)
                
                rx = nx
                ry = ny
                break
    else:
        for j in range(len(keyboard)):
            if i in keyboard[j]:
                nx = j
                ny = keyboard[j].index(i)
                
                time += abs(nx - lx) + abs(ny - ly)
                
                lx = nx
                ly = ny
                break

print(time)

# left, right = input().split()
# strings = list(input())

# keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
# mo = 'yuiophjklbnm'

# xl, yl, xr, yr = None, None, None, None

# for i in range(len(keyboard)):
#     if left in keyboard[i]:
#         xl = i
#         yl = keyboard[i].index(left)

#     if right in keyboard[i]:
#         xr = i
#         yr = keyboard[i].index(right)

# time = 0
# for string in strings:
#     time += 1
#     if string in mo:
#         for i in range(len(keyboard)):
#             if string in keyboard[i]:
#                 nx = i
#                 ny = keyboard[i].index(string)

#                 time += abs(nx - xr) + abs(ny - yr)
#                 xr = nx
#                 yr = ny
#                 break
#     else:
#         for i in range(len(keyboard)):
#             if string in keyboard[i]:
#                 nx = i
#                 ny = keyboard[i].index(string)

#                 time += abs(nx - xl) + abs(ny - yl)
#                 xl = nx
#                 yl = ny
#                 break

# print(time)