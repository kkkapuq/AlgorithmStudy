'''
1. 투포인터로 순회, left, i, right 를 더해주고, 해당 값이 target의 근사값 closest의 절대값보다 작으면 closest 교체
2. closest return 해주면될듯?
'''
def threeSumClosest(nums: list[int], target: int):
    answer = 0
    nums.sort()
    closest = float('inf')
    
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            threeSum = nums[left] + nums[i] + nums[right]
            if threeSum == target:
                return target
            if abs(closest) > abs(target - threeSum):
                closest = target - threeSum
            if target > threeSum:
                left += 1
            else:
                right -= 1
    
    return print(target - closest)
    
    # diff = float('inf')
    # nums.sort()
    # for idx,a in enumerate(nums):
    #     l,r = idx +1, len(nums)-1
    #     while l < r :
    #         three_sum = a + nums[l] + nums[r]
    #         if abs(target - three_sum) < abs(diff):
    #             diff = target - three_sum
    #         if three_sum > target:
    #             r -= 1
    #         else:
    #             l += 1
    #     if diff == 0 :
    #         break
    # return target- diff
    
    
threeSumClosest([-1,2,1,-4], 1)