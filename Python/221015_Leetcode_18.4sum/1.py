def fourSum(nums: list[int], target: int):
    n = len(nums)
    nums.sort()
    answer = set()
    for i in range(n):
        for j in range(i+1, n):
            # 투포인터를 이렇게 잡는 이유는 i와 j 와 j안에서 도는 투포인터에서 도출되는 값을 결과값으로 만들기 위함임.
            l, r =  j+1, n-1
            remain = target - nums[i] - nums[j]
            while(l < r):
                if remain == nums[l] + nums[r]:
                    answer.add((nums[i], nums[j], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < remain:
                    l += 1
                else:
                    r -= 1
    
    return answer
            

def twoSum(nums, l, r, i, j, target):
    remain = target - nums[i] - nums[j]
    while(l < r):
        if nums[l] + nums[r] == remain:
            l += 1
            r -= 1
            return (nums[l], nums[r], nums[i], nums[j])
        elif nums[l] + nums[r] < remain:
            l += 1
        else:
            r -= 1

fourSum([1,0,-1,0,-2,2], 0)