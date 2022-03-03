import sys
read = sys.stdin.readline

n = int(read())
m = int(read())
inf = int(1e9)

graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    if c < graph[a][b]:
        graph[a][b] = c
        
for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            graph[i][j] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print()
