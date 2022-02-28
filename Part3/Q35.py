n = int(input())

dp = [0] * n
dp[0] = 1
# 2, 3, 5를 곱할 인덱스
i2 = i3 = i5 = 0

# 다음에 2, 3, 5를 곱해서 나올 수
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    # 다음에 2, 3, 5를 곱해서 나올 수 중에서 가장 작은 수 선택
    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
        
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3

    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])
