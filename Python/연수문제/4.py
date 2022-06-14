def solution(words):
    answer = [] * len(words)
    
    if len(words) < 2:
        return print(words[0])
    
    for i in range(len(words)):
        if i == len(words) - 2:
            answer.append(words[i])
        elif i == len(words) - 1:
            answer.append(' and ' + words[i])
        else:
            answer.append(words[i] + ', ')
    return print(''.join(answer))

words = list(input().split(' '))

solution(words)