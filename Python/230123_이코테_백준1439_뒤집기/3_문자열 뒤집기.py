s = input()

'''
1. 0과 1중 뭐로 바꾸는게 더 빠른지 판단
2. 연속된 문자열만 바꿀 수 있는거 고려
'''
toZero, toOne = 0, 0

# 첫 글자 시작문자에 따라 변경
if s[0] == '0':
    toOne += 1
else:
    toZero += 1
    
# 1로 바꾸는 경우
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    elif s[i] != s[i+1] and s[i] == '0':
        toOne += 1
        
# 0으로 바꾸는 경우 
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    elif s[i] != s[i+1] and s[i] == '1':
        toOne += 1
print(min(toZero, toOne))