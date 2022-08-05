def lengthOfLongestSubstring(s: str):
    window = set()
    l = 0
    res = 0
    
    for i in range(len(s)):
        while s[i] in window:
            window.remove(s[l])
            l += 1
        window.add(s[i])
        res = max(res, i - l + 1)
    return res
            

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