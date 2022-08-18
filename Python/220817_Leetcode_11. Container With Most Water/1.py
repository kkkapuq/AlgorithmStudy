'''
1. 가장 큰 수를 골라서
'''
def maxArea(height: list[int]):
    # 시간초과 풀이
    # maximum = 0
    # tempHeight = 0
    
    # for i in range(len(height)):
    #     for j in range(i+1, len(height)):
    #         if height[i] > height[j]:
    #             tempHeight = height[j]
    #         else:
    #             tempHeight = height[i]
    #         amount = tempHeight * abs(i - j)
    #         if maximum < amount:
    #             maximum = amount
    
    maximum = 0
    tempHeight = 0
    left, right = 0, len(height)-1
    
    while left < right:
        if height[left] < height[right]:
            tempHeight = height[left]
            amount = height[left] * abs(left - right)
            maximum = max(amount, maximum)
            left += 1
        else:
            tempHeight = height[right]
            amount = height[right] * abs(left - right)
            maximum = max(amount, maximum)
            right -= 1
    
    return maximum
    
    
maxArea([1,8,6,2,5,4,8,3,7])