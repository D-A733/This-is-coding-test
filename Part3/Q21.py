from collections import deque
import sys
read = sys.stdin.readline

n, L, R = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(n)]

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(A, start, check):
    result = [start]
    q = deque([start])
    population = A[start[0]][start[1]] # 연합의 인구 총합
    unite = 1 # 연합의 개수
    check[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는 경우, 이미 방문했던 노드 제외
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 or check[nx][ny]:
                continue
            if L <= abs(A[nx][ny] - A[x][y]) and abs(A[nx][ny] - A[x][y]) <= R:
                q.append((nx,ny))
                result.append((nx,ny))
                check[nx][ny] = True
                population += A[nx][ny]
                unite += 1
    for x, y in result:
        A[x][y] = population // unite
    return unite - 1 # 연합이 있는지 확인용

count = 0
while True:
    break_point = 0
    check = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                break_point += bfs(A, (i,j), check)

    if not break_point: # bfs결과 연합이 없으면 멈추기
        break
    count += 1
    
print(count)
