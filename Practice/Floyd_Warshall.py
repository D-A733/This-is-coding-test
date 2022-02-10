import sys
inf = int(1e9)
read = sys.stdin.readline
n, m = map(int, read().split())
graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, read().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n+1):
    graph[i][i] = 0

x, k = map(int, read().split())

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

time = graph[1][k] + graph[k][x]
if time > inf:
    print(-1)
else:
    print(time)
