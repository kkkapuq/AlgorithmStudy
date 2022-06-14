# print('Please insert your departure spot : ')
# departure = input()

# print('Please insert your destination spot : ')
# destination = input()

# print('Please insert information\'s size : ')
# n = int(input())

# print('Please insert departure, destination, cost : ')
# graph = [ list(map(str, input().split())) for _ in range(n) ]

info = [
    ( 'JFK', 'ATL', 150 ),
    ( 'ATL', 'SFO', 400 ),
    ( 'ORD', 'LAX', 200 ),
    ( 'LAX', 'DFW', 80 ),
    ( 'JFK', 'HKG', 800 ),
    ( 'ATL', 'ORD', 90 ),
    ( 'JFK', 'LAX', 500 )
]

departure = input()
destination = input()
costList = []

for i in range(len(info)):
    for j in range(len(info)):
        if info[i][0] == departure and info[j][1] == destination:
            costList.append(info[i][2])

print(costList)