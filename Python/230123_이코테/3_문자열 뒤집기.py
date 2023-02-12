s = input()

'''
1. 0과 1중 뭐로 바꾸는게 더 빠른지 판단
2. 연속된 문자열만 바꿀 수 있는거 고려
'''
'''
# 내 풀이
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

'''

s = input()
count = 0

# 현재 수에서 다음 값이 변화할 때만 세어주고, 0이나 1 둘 중 하나로 출력되면 되니까 //2 해주면 된다.
# count + 1 // 2 에서 count + 1 해주는 이유는..?
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
print(count // 2)