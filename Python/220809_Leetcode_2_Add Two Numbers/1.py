from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        stack = []
        
        if l1 == [0] and l2 == [0]:
            return [0]
        
        answerNode = ListNode()
        str1, str2 = [], []
        while l1:
            str1.append(str(l1.val))
            l1 = l1.next
        while l2:
            str2.append(str(l2.val))
            l2 = l2.next
        
        str1.reverse()
        str2.reverse()
        str1 = ''.join(str1)
        str2 = ''.join(str2)
        answer = str(int(str1) + int(str2))
        temp = answerNode
        for i in answer[::-1]:
            temp.next = ListNode()
            temp = temp.next
            temp.val = int(i)
            
        return answerNode.next
        
        
        list1 = l1.val
        list2 = l2.val
        
        list1.reverse()
        list2.reverse()
        str1 = ''.join(map(str, list1))
        str2 = ''.join(map(str, list2))
        
        answer = int(str1) + int(str2)
        answer = str(answer)
        
        for i in answer:
            stack.append(int(i))
        
        stack.reverse()
        
        return stack
    
    
# temp = Solution()
        
node1 = ListNode([2,4,3])
node2 = ListNode([5,6,4])

# temp.addTwoNumbers(node1, node2)

# node1.next = node2
# head = node1

# print(node1.val)
# print(node2.val)
# print(node1.next.val)

# str1 = [2,4,9]
# str2 = [5,6,4,9]

# # result = str(int(num1[::-1]) + int(num2[::-1]))
# str1 = ''.join(map(str, str1))
# str2 = ''.join(map(str, str2))
# answer = str(int(str1) + int(str2))
# print(answer)