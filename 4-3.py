n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 맵을 입력받아 저장
data = [list(map(int, input().split())) for _ in range(n)]

# 방문한 적 있는 좌표를 기록
visited = data
visited[x][y] = 1

left = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back = [(0, -1), (-1, 0), (0, 1), (1, 0)]
count = 1

while 1:
    # 각 방향에 대해 왼쪽방향, 뒤쪽방향의 좌표
    lx = x + left[d][0]
    ly = y + left[d][1]
    
    # 네 방향 모두 이미 가본 칸이거나 바다인 경우
    if (visited[x-1][y],visited[x+1][y],visited[x][y-1],visited[x][y+1]) == (1,1,1,1):
        bx = x + back[d][0]
        by = y + back[d][1]
        # 뒤쪽 방향이 바다인 경우
        if data[bx][by] == 1:
            break
        # 뒤쪽 방향이 바다가 아닌경우
        else:
            x, y = bx, by
            continue
    # 왼쪽 방향에 방문하지 않은 칸이 있는 경우
    if visited[lx][ly] == 0:
        visited[lx][ly] = 1
        count += 1
        x, y = lx, ly
        d = (d + 3) % 4
    # 왼쪽 방향에 방문하지 않은 칸이 없는 경우
    else:
        d = (d + 3) % 4
print(count)
