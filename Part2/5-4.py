from collections import deque
n, m = map(int, input().split())
# 2차원 미로 정보 입력받기
maze = [list(map(int, input())) for _ in range(n)]

# 이동할 방향 정의(상, 하, 좌, 우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나거나 괴물이 있는 곳은 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maze[nx][ny] == 0:
                continue
            # 처음 방문한 경우에만 기록
            if maze[nx][ny] == 1:
                queue.append((nx,ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[n-1][m-1]

print(bfs(0,0))
    
