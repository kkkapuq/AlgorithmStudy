def lengthOfLongestSubstring(s: str):
    lengthList = [0]
    stack = []
    strList = list(s)
    
    if len(s) == 1:
        return 1
    
    for i in range(len(s)):
        if s[i] in stack:
            lengthList.append(len(stack))
            stack = []
            stack.append(s[i])
        else:
            stack.append(s[i])
            if len(stack) > max(lengthList):
                lengthList.append(len(stack))
    
    return print(max(lengthList))

lengthOfLongestSubstring('dvdf')

'''
def lengthOfLongestSubstring(s: str):
    stack = []
    tempStack = []
    answerStack = []
    strList = list(s)
    flag = 0

    for i in strList:
        if i in stack:
            
            if i in tempStack:
                tempStack.pop()
                if tempStack > stack:
                    answerStack = tempStack
                    stack = []
                else:
                    answer = stack
                    tempStack = []
            else:
                tempStack.append(i)
        else:
            if flag == 0:
                stack.append(i)
            
    return print(len(answerStack))
            
lengthOfLongestSubstring('pwwkefgw')
'''