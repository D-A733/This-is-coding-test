import sys
read = sys.stdin.readline
inf = int(1e9)
# 노드, 간선의 개수 입력받기
n, m = map(int, read().split())
# 그래프 입력받기
graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n+1):
    graph[i][i] = 0
# x, k 입력받기
x, k = map(int, read().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][x] + graph[x][k]
if distance >= inf:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
