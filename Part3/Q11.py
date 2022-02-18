from collections import deque
import sys

read = sys.stdin.readline
n = int(read())
k = int(read())
# 빈칸은 0, 벽은 1로 표시
game_map = [[1] * (n+2) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, n+1):
        game_map[i][j] = 0

# 사과의 위치는 2로 표시
for _ in range(k):
    x, y = map(int, read().split())
    game_map[x][y] = 2

rotate = 0 # 현재 보고 있는 방향, 초기값 오른쪽
# 방향 변환 정보
rotate_data = []
l = int(read())
for _ in range(l):
    x, c = read().split()
    rotate_data.append((int(x), c))

# 오른쪽, 아래, 왼쪽, 위 순서
d = [(0,1), (1, 0), (0, -1), (-1, 0)]

# snake의 위치를 큐에 저장
snake = deque([(1,1)])
time = 0

while True:
    for x, c in rotate_data:
        if time == x:
            rotate = (rotate + 1) % 4 if c == "D" else (rotate + 3) % 4
            break
    time += 1
    nx = snake[0][0] + d[rotate][0]
    ny = snake[0][1] + d[rotate][1]
    if game_map[nx][ny] == 1 or (nx,ny) in snake:
        break
    elif game_map[nx][ny] == 2:
        snake.appendleft((nx,ny))
        game_map[nx][ny] = 0
    else:
        snake.appendleft((nx,ny))
        snake.pop()
print(time)

    

    
