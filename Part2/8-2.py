import sys
x = int(sys.stdin.readline().rstrip())
dp = [0] * (x+1)
for i in range(2,x+1):
    s = [dp[i-1]]
    if i % 5 == 0:
        s.append(dp[i//5])
    if i % 3 == 0:
        s.append(dp[i//3])
    if i % 2 == 0:
        s.append(dp[i//2])
    dp[i] = min(s) + 1
print(dp[x])
