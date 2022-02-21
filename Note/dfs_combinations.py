def dfs(level, beginwith):
    if level == r: # r개를 다 뽑은 경우
        print(result)
        return
    for i in range(beginwith, len(n)):
        result[level] = n[i]
        dfs(level + 1, i + 1)

n = [i for i in range(10)]
r = 6 # 6개 뽑기
result = [0] * r
dfs(0,0)
