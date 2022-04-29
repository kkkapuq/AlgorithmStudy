n = 1260

coin = [500, 100, 50, 10]
cnt = 0

for i in coin:
    cnt += n // i
    n %= i
    
print(cnt)