a, b, c = map(int, input().split())

#분할정복으로 계산, 짝수와 홀수로 나눠서 하자
def mul(a, b):
    if b == 1:
        return a & c
    #짝수라면
    elif b % 2 == 0:
        temp = mul(a, b//2)
        return temp*temp%c
    #홀수라면
    elif b % 2 == 1:
        temp = mul(a, (b-1)//2)
        return (temp*temp*a)%c

print(mul(a, b))