
def findMedianSortedArrays(nums1: list[int], nums2: list[int]):
    mergedList = nums1 + nums2
    if len(mergedList) == 0:
        return []
    
    mergedList.sort()
    
    if len(mergedList) % 2 != 0:
        return mergedList[(0 + len(mergedList) - 1) // 2]
    
    else:
        temp1 = int((0 + len(mergedList) - 1) / 2 - 0.5)
        temp2 = int((0 + len(mergedList) - 1) / 2 + 0.5)
        answer = (mergedList[temp1] + mergedList[temp2]) / 2
        return answer
    
findMedianSortedArrays([1, 1], [1, 2])