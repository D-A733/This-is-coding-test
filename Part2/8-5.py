import sys
read = sys.stdin.readline
n, m = map(int, read().split())
coin = [int(read().rstrip()) for _ in range(n)]
dp = [10001] * 10001
for i in coin:
    dp[i] = 1
for i in range(1, m+1):
    if dp[i] == 1:
        continue
    try:
        a = 10001
        for k in coin:
            a = min(dp[i - k], a)
        dp[i] = a + 1
    except IndexError as Exception:
        print(i)
        continue

if dp[m] > 10000:
    print(-1)
else:
    print(dp[m])
            
