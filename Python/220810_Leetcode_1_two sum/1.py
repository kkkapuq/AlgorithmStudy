def twoSum(nums: list[int], target: int):
    dic = {}
    answerList = []
    
    for i in range(len(nums)):
        dic[nums[i]] = i
        
    for i, n in enumerate(nums):
        if target - n in dic and i != dic[target-n]:
            answerList.append(i)
            answerList.append(dic[target-n])
            return answerList
    

twoSum([3,2,4], 6)