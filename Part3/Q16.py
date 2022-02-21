import sys
from collections import deque
from itertools import combinations
import copy
read = sys.stdin.readline
n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]

# 바이러스, 빈칸, 벽의 좌표 정보
virus = []
virus_count = 0
blank = []
wall = []
wall_count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i,j))
        elif graph[i][j] == 1:
            wall.append((i,j))
            wall_count += 1
        else:
            virus.append((i,j))
            virus_count += 1
# 남, 동, 북, 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(graph, start):
    a, b = start
    q = deque([(a,b)])
    spread_count = 0
    while q:
        x, y = q.popleft()
        # 4방향에 대해 모두 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1: # 범위를 벗어가는 경우 제외
                continue
            else:
                if graph[nx][ny] == 0: # 빈칸을 만나면 전염
                    graph[nx][ny] = 2
                    q.append((nx,ny))
                    spread_count += 1
                else: # 벽이나 이미 전염된 곳은 스킵
                    continue
    return spread_count
blank_count = 0
# 빈칸중에서 벽을 3개 세우는 모든 경우의 수 확인
for candidate in list(combinations(blank, 3)):
    graph_candidate = copy.deepcopy(graph)
    for x, y in candidate: # 3개의 벽 설치하기
        graph_candidate[x][y] = 1
    spread_count = 0
    for point in virus: # 바이러스 전염시키기
        spread_count += bfs(graph_candidate, point)

    # 빈칸의 개수를 조사해서 최댓값을 저장
    blank_count = max(blank_count, n*m - (wall_count + 3) - (virus_count + spread_count))

print(blank_count)
