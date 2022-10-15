def minPathSum(grid: list[list[int]]):
    # 행, 열
    n = len(grid)
    m = len(grid[0])
    minimum = 0
    
    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0:
                # 오른쪽으로 움직이거나 아래로 내려오는 방법 만으로 목적지까지 도달하는 것이 규칙이다.
                # 따라서, for문이 끝날때까지 grid[i][j]를 최소값으로 그려주면 되는거아닐까?
                minimum = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])
                grid[i][j] = minimum
            
            # 윗 자리에 있는 애 더해주기
            elif i > 0:
                grid[i][j] += grid[i-1][j]
            # 왼쪽에 있는 애 더해주기
            else:
                grid[i][j] += grid[i][j-1]
    
    return grid[n-1][m-1]

minPathSum([[1,3,1],[1,5,1],[4,2,1]])