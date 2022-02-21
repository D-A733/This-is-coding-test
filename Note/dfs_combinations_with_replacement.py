result = []
def dfs(idx, count):
    if count == m:
        print(result)
        return
    for i in range(idx, n):
        result.append(i+1)
        dfs(i, count+1)
        result.pop()
m = 3 # 3개 뽑기
n = 4 # 1 ~ 4 중에서
dfs(0,0)
