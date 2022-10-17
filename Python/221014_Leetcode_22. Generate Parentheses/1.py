
def generateParenthesis(n: int):
    left = right = 0
    paren = ''
    global answer
    answer = []
    
    parenthesis(left, right, paren, n)
    return answer

def parenthesis(left, right, paren, n):    
    
    if left == n and right == n:
        answer.append(paren)
        return
    
    if left < n:
        parenthesis(left+1, right, paren + '(', n)
    
    
    if left > right:
        parenthesis(left, right+1, paren + ')', n)
        
        
print(generateParenthesis(3))