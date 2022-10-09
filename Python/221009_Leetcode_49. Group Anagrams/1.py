def groupAnagrams(strs: list[str]):
    
    if len(strs) == 1:
        return [strs]
    
    answerDict = {}
    
    for i in strs:
        sortedString = ''.join(sorted(i))
        
        if sortedString not in answerDict:
            answerDict[sortedString] = []
        answerDict[sortedString].append(i)
        
    return list(answerDict.values()) 

groupAnagrams(["eat","tea","tan","ate","nat","bat"])