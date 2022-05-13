str = list(input().rstrip())
stack = []
operator = ['+', '-', '*', '/', '(', ')']
# 우선순위는 괄호 > *, / > +, -
answer = '';

for i in str:
    # 연산자가 아니라면 정답문자열에 추가
    if i not in operator:
        answer += i
    else:
        # 여는 괄호는 스택에 추가
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            # 스택의 마지막 인덱스가 *, / 이라면 정답문자열에 추가해주기 ( +, - 보다 우선이니까 )
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            # +, - 보다 낮은 우선순위는 없으므로, 여는 괄호를 제외한 연산자면 넣어주기
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            # 닫는 괄호면 그동안 모아온 연산자들 다 반환
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()
print(answer)