import sys
read = sys.stdin.readline
n, m = map(int, read().split())
inf = int(1e9)
graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, read().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n+1):
    graph[i][i] = 0
    
x, k = map(int, read().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] + graph[k][x] > inf:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
