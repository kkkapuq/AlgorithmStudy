from sys import stdin

input = stdin.readline

a, b, c = map(int, input().split())

# 모듈러 곱셈법칙
#   a*b % c == (a % c * b % c) % c

# 모듈러, 지수 법칙 응용
#   a^5 % c == a^2 * a^2*a %c
#           == (a^2 % c * a^2*a % c) % c 

def modular_def(a, b, c):
    if b == 1:
        return a % c
    temp = modular_def(a, int(b/2), c)
    
    # 지수법칙 a^7 = a^3 * a^3 * a
    # 지수가 짝수
    if num2 % 2 == 0:
        return temp * temp % c
    # 홀수
    else:
        return temp * temp * a % c
        
print(modular_def(a, b, c))
