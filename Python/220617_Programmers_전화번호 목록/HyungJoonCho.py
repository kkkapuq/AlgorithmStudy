'''
1. 최근에 푼 접두어랑 동일한 문제.
2. 글자 길이 오름차순으로 sort 해주고, 현재 단어 (j) 가 다른 단어(i) 의 0~i 번째 인덱스까지 같다면 false 로 return 해주자
'''
'''
잘못된 풀이, 시간초과 남
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    hashMap = {}
    
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    
    return answer
'''
'''
# 딕셔너리를 활용한 풀이
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    hashBook = {}
    
    for i in phone_book:
        hashBook[i] = 1
    
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in hashBook and temp != i:
                return False
    
    return answer
'''
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    #
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer
    
    return answer

solution(["119", "97674223", "1195524421", "1129432", "112"])