def groupAnagrams(strs: list[str]):
    
    
    
    answerDic = {}
    for i in strs:
        sortedString = ''.join(sorted(i))
        if sortedString not in answerDic:
            answerDic[sortedString] = []
        answerDic[sortedString].append(i)
    
    print (list(answerDic.values()))
    
    
    

groupAnagrams(["eat","tea","tan","ate","nat","bat"])