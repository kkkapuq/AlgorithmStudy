from sys import stdin

input = stdin.readline

a, b, c = map(int, input().split())

# ��ⷯ ������Ģ ����
#   a*b % c == (a % c * b % c) % c

def modular_def(a, b, c):
    if b == 1:
        return a % c
    temp = modular_def(a, int(b/2), c)
    
    # ������Ģ ���� a^7 = a^3 * a^3 * a
    # ������ ¦��
    if num2 % 2 == 0:
        return temp * temp % denominator
    # Ȧ��
    else:
        return temp * temp * num1 % denominator
        
print(modular_def(a, b, c))