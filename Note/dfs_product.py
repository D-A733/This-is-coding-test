def dfs(level):
    if level == r:
        print(result)
        return
    for i in n:
        result.append(i)
        dfs(level + 1)
        result.pop()
        
n = [i for i in range(1, 4)]
r = 3
result = []
dfs(0)
