def canJump(nums: list[int]):
    maxIndex = 0
    for i in range(len(nums)):
        maxIndex = max(maxIndex, i+nums[i])
        if maxIndex >= len(nums)-1:
            return True
    return False
    
canJump([0])