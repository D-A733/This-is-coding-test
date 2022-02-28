import sys
read = sys.stdin.readline

n = int(read())
T = [0]
P = [0]

for _ in range(n):
    t, p = map(int, read().split())
    T.append(t)
    P.append(p)

# i일 까지 했을 때 얻을 수 있는 최대 수익
dp = [0] * (n + 1)

# i일에 끝나는 상담 정보
indegree = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    if T[i] + i - 1 <= n: # n일이 넘어가는 경우 제외
        indegree[T[i] + i - 1].append(i)

for i in range(1, n+1):
    max_value = dp[i-1]
    if indegree[i] != []: # indegree가 비어있지 않다면
        for x in indegree[i]:
            max_value = max(max_value, dp[x-1] + P[x])
    dp[i] = max_value

print(dp[n])
