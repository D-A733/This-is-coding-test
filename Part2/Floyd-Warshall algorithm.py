import sys
read = sys.stdin.readline
n, m = map(int, read().split())
inf = int(1e9)
# 그래프를 inf로 초기화
graph = [[inf]*(n + 1) for _ in range(n + 1)]

# 그래프 정보 입력받기
for _ in range(m):
    # a에서 b로 가는 비용이 c
    a, b, c = map(int, read().split())
    graph[a][b] = c

# 자기 자신으로 가는 비용은 0으로 설정
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행한 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            print("inf", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
