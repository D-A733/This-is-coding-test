import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)
dp[1:3] = [1,3]
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796
print(dp[i])
