def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # dp테이블 초기 설정
    for i in range(m + 1):
        dp[0][i] = i
    for j in range(n + 1):
        dp[j][0] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i-1] == str2[j-1]: # 두 문자가 같은 경우
                dp[i][j] = dp[i-1][j-1]
            else: # 두 문자가 다른 경우
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
    return dp[n][m]

A = input()
B = input()

print(edit_dist(A,B))
