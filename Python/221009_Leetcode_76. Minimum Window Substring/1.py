import collections
from typing import Counter

def minWindow(s: str, t: str):
    '''
    if not s or not t or len(s) < len(t):
        return ''
    
    # 문자별 가지고 있는 개수
    count = collections.Counter(t)
    # 키의 개수
    missing = sum(count.values())
    
    left = right = start = end = 0
    for right, nums in enumerate(s, 1):
        # right -= 1
        if count[nums] > 0 :
            # 이부분을 왜 빼주는거임??????
            missing -= 1
        count[nums] -= 1
        # 이게 의미하는 바가 뭔지를 모르겠음... missing이 갯수가 0이면 문자열을 다 포함하고 있다는뜻?
        if missing == 0:
            while left < count[s[left]] < 0:
                count[s[left]] += 1
                left += 1
            if not end or (end - start) > (right - left):
                start, end = left, right
            count[s[left]] += 1
            left += 1
            missing += 1
    return s[start:end]
                
     '''
    # t가 s보다 크면 '' return
    if len(t) > len(s): return ""
    
    # 얘는 왜 len(s) 보다 크게 설정하는건지 ?
    minLength = len(s) + 1
    
    # t에서 문자별로 갖고있는 개수
    count = Counter(t)
    
    # t의 문자별 개수
    # distincts로 하여금, 현재 t 문자열이 s문자열에 다 포함되었는지는 0으로 판단하는 변수가 되는 것이다.
    # 아래에서 count[s[j]] == 1일때 +=1 해주는 이유는
    # 우리가 s[i:j] 의 문자열에서 t문자열 중의 한 단어를 추가로 찾아야 한다는 말이 되기 때문이다.
    # 그래서 distincts가 0일 때 while문을 타는 이유는, 현재 문자열에서 t문자열 포함 조건을 만족시켰다는 뜻이며
    # 이 문자열 윈도우 안에서 더 적은 윈도우 값을 찾아내기 위한 조건문이다.
    distincts = len(count)
    
    # 투포인터용 변수
    i,j = 0,0
    
    # 최소 window에서 사용될 변수
    minI = -1
    minJ = -1
    
    
    while j < len(s):
        if s[j] in count:
            count[s[j]] -= 1
            # 얘는 왜 빼주는거임..???
            if count[s[j]] == 0: distincts -= 1
        
        # 만약 현재 윈도우에서 t가 있다는 조건이 성립한다면 
        # 최소 문자열을 찾는 과정
        # 근데 distincts가 뭐때문에 0일때 비교해야 하는건지를 모르겠음...
        while distincts == 0:
            # 현재 윈도우의 크기가 이전 유효 윈도우 크기 값보다 적은 경우 더 적은값이 나올수있나 계산해보기
            if j - i + 1 < minLength:
                minLength = j - i + 1
                minI = i
                minJ = j
            if s[i] in count: 
                count[s[i]] += 1
                # 이 distincts가 무슨 역할을 하는건지 이해가 안간다..;;
                if count[s[i]] == 1 : distincts += 1
            
            i += 1
        
        # right pointer 늘려주기
        j += 1
    
    # 정답 도출
    substring = s[minI:minJ + 1]
    
    return substring

minWindow("ADOBECODEBANC", 'ABC')