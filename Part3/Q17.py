from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
graph = [[-1] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][1:] = list(map(int, read().split()))
    
s, x, y = map(int, read().split())

# 바이러스 좌표 및 종류 정보
virus = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j]:
            virus.append((i, j, graph[i][j]))

# virus의 종류가 낮은 것부터 전염
virus.sort(key=lambda x: x[2])

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

time = 1
next_q = deque(virus)
q = deque()
while time <= s:
    q = next_q
    next_q = deque()
    while q: # 매초 바이러스 전염 반복
        a, b, k = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 범위를 벗어나면 통과
            if nx < 1 or nx > n or ny < 1 or ny > n :
                continue
            # 빈칸인 경우 k바이러스로 전염
            if graph[nx][ny] == 0:
                graph[nx][ny] = k
                next_q.append((nx,ny,k))
    time += 1

print(graph[x][y])
