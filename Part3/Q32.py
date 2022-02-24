import sys
read = sys.stdin.readline

n = int(read())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, read().split())))

dp = [[0] * i for i in range(1, n+1)]

dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 가장 왼쪽에 있는 수는 경우의 수가 한가지
            dp[i][j] = dp[i-1][j]
        elif j == i: # 가장 오른쪽에 있는 수는 경우의 수가 한가지
            dp[i][j] = dp[i-1][j-1]
        else: # 나머지 경우는 경우의 수가 두가지
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
        dp[i][j] += triangle[i][j]

print(max(dp[-1]))
