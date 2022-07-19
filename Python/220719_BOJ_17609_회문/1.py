'''
1. 일반적인 회문 판단 함수, 정답을 출력하는 함수 두개로 나뉘어서 작업해주자
2. 처음엔 for문으로 완탐했는데, 시간초과가 나서 투포인터로 바꿈.
3. 왼쪽과 오른쪽 모두 회문 여부를 판단해보고, 둘중 하나라도 회문이라면 1로 노출, 아니면 2로 하는 방식으로 진행
'''
import sys

t = int(input())

# 0, 1, 2중 하나 출력해주는 함수
def palindrome(string, left, right):
    if isPalindrome(string, left, right):
        return print(0)
    else:
        while left < right:
            # 문자열의 left인덱스와 right 인덱스가 같다면 left는 늘리고 right 는 줄인다.
            if string[left] == string[right] :
                left += 1
                right -= 1
            # 만약 같지 않다면, 현재 left 인덱스보다 +1 한놈과, right인덱스보다 -1 한놈을 둘다 회문 여부 판단하는 함수로 보낸다.
            # 둘 중 하나라도 회문이 되면 1 출력하고 끝
            else:
                leftPal = isPalindrome(string, left + 1, right)
                rightPal = isPalindrome(string, left, right - 1)
                
                if leftPal or rightPal:
                    return print(1)
                else:
                    return print(2)
    
# 팰린드롬 여부를 판단하는 함수
def isPalindrome(string, left, right):
    str = list(string)
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

for i in range(t):
    string = sys.stdin.readline().rstrip()
    left = 0
    right = len(string) - 1
    palindrome(string, left, right)
