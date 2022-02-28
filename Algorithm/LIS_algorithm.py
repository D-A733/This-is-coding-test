# LIS(Longest Increasing Subsequence) 문제
# 전형적인 Dynamic Programming 문제 유형
# 주어진 수열에서 가장 긴 증가하는 부분수열의 길이 구하기
n = 6
array = [10, 20, 10, 30, 20, 50]

# dp[i]는 array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 최솟값 1을 기본값으로 세팅
dp = [1] * 6

for i in range(n):
    for j in range(i):
        # i번째 원소보다 작은 수에 대해서만 확인
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
