'''
첫 풀이, 개같이 멸망함..
t = int(input())

for _ in range(t):
    n = int(input())
    list = [] * n
    answer = []
    num = [1, 2, 3]
    
    for i in range(len(list)):
        temp = []
        
        for j in num:
            while True:
                temp.append(j)
                if sum(temp) > n:
                    del temp[len(temp) - 1]
                    break
'''

'''   
1 -> [1] = 1개
2 -> [1, 1] [2] = 2개
3 -> [1, 1, 1] [1, 2] [2, 1] [3] = 4개
4 -> [1, 1, 1, 1] [1, 1, 2] [1, 2, 1] [2, 1, 1] [2, 2] [3, 1] [1, 3] = 7개
5 -> [1, 1, 1, 1, 1] [1, 1, 1, 2] [1, 1, 2, 1] [1, 2, 1, 1] [2, 1, 1, 1] [2, 1, 2] [2, 2, 1] [1, 2, 2] [2, 3] [3, 2] [3, 1, 1] [1, 3, 1] [1, 1, 3] = 13개

f(n) = f(n-1) + f(n-2) + f(n-3)
'''
import sys
sys.setrecursionlimit(10000)

t = int(input())

def recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recursion(n-1) + recursion(n-2) + recursion(n-3)

for _ in range(t):
    n = int(input())
    print(recursion(n))