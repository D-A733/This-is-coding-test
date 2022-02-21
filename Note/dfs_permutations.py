def dfs(level):
    if level == r: # 4개를 뽑은 경우
        print(result)
        return
    for i in range(len(n)):
        if checked[i]: # i를 앞에서 뽑았으면 스킵
            continue
        result[level] = n[i]
        checked[i] = True
        dfs(level + 1)
        checked[i] = False

n = [i + 1 for i in range(3)]
r = 2 # r개 뽑기
result = [0] * r
checked = [False] * len(n)
dfs(0)
