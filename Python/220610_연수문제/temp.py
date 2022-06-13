'''
1. 10번 반복
2. len(list) > 3 일 때, list[:3] 의 원소가 모두 동일하면 break
'''

from random import randint

# 평균값을 구할 sum 선언
sum = 0

for i in range(10):
    # flip 수 선언, coinList for문 한번 돌때마다 초기화
    cnt = 0
    coinList = []
    while True:
        temp = randint(0, 1)
        if temp == 0:
            temp = 'T'
        else:
            temp = 'H'
        coinList.append(temp)
        
        tempSet = set(coinList[-3:])
        
        cnt += 1
        
        if len(coinList) > 2 and len(tempSet) < 2:
            sum += cnt
            break
    print(' '.join(coinList) + ' ' + str(cnt) + ' flips')

print('On average, ' + str(sum / 10) + ' flips were needed.')
