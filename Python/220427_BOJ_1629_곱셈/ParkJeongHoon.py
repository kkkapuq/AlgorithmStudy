from sys import stdin

input = stdin.readline

num1, num2, denominator = map(int, input().split())
"""
ab mod p
(a mod p * b mod p)mod p
a = a//p + a mod p
b = b//p + b mod p
ab = a//p * b//p + a mod p * b//p + a//p * b mod p + a mod p * b mod p
ab mod p = (a mod p * b mod p) mod p
math.sqrt(ab) * math.sqrt(ab) 
"""


def get_half(num1, num2, denominator):
    if num2 == 1:
        return num1 % denominator
    temp = get_half(num1, int(num2/2), denominator)
    if num2 % 2 == 0:
        return temp * temp % denominator
    else:
        return temp * temp * num1 % denominator
print(get_half(num1, num2, denominator))



