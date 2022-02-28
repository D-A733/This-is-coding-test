import sys
read = sys.stdin.readline

n = int(read())
power = list(map(int, read().split()))

# LIS(Longest Increasing Subsequence) 유형
dp = [1] * n
for i in range(n):
    for j in range(i):
        if power[j] > power[i]:
            dp[i] = max(dp[i], dp[j] + 1) 
        
print(n - max(dp))
