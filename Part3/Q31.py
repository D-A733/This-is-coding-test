import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t): # t번 반복
    n, m = map(int, read().split())
    data = []
    mine = list(map(int, read().split()))
    for i in range(n):
        data.append(mine[m * i:m * (i + 1)])
    
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = data[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0: # 맨 위의 행의 경우 2가지 선택지
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1])
            elif i == n - 1: # 맨 밑의 행의 경우 2가지 선택지
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1])
            else: # 나머지의 경우 3가지 선택지
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
            dp[i][j] += data[i][j]
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][-1])
    print(result)
