import sys
read = sys.stdin.readline
n = int(read().rstrip())
food = [0] + list(map(int, read().split()))
dp = [0] * (n+1)
dp[1:3] = food[1:3]
for i in range(3, n+1):
    dp[i] = max(dp[i-2], dp[i-3]) + food[i]
print(dp[i])
