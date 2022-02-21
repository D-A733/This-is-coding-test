from collections import deque
import sys
read = sys.stdin.readline
n = 5
board = [[1,1,1,1,1,1,1],
         [1,0,0,0,1,1,1],
         [1,0,0,0,1,0,1],
         [1,0,1,0,1,1,1],
         [1,1,1,0,0,1,1],
         [1,0,0,0,0,0,1],
         [1,1,1,1,1,1,1]]

def get_next_pos(now, board):
    next_pos = []
    leg1, leg2 = now
    leg1_x, leg1_y = leg1
    leg2_x, leg2_y = leg2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        next_leg1_x, next_leg1_y, next_leg2_x, next_leg2_y = leg1_x+dx[i], leg1_y+dy[i], leg2_x+dx[i], leg2_y+dy[i]
        if board[next_leg1_x][next_leg1_y] == 0 and board[next_leg2_x][next_leg2_y] == 0:
            next_pos.append({(next_leg1_x,next_leg1_y),(next_leg2_x,next_leg2_y)})
    
    if leg1_x == leg2_x: # 가로방향인 경우
        if board[leg1_x - 1][leg1_y] == 0 and board[leg2_x - 1][leg2_y] == 0: # 상
            next_pos.append({(leg1_x,leg1_y),(leg1_x-1,leg1_y)}) # 위로 반시계방향 회전
            next_pos.append({(leg2_x-1,leg2_y),(leg2_x,leg2_y)}) # 위로 시계방향 회전
        if board[leg1_x + 1][leg1_y] == 0 and board[leg2_x + 1][leg2_y] == 0: # 하
            next_pos.append({(leg1_x,leg1_y),(leg1_x+1,leg1_y)}) # 아래로 시계방향 회전
            next_pos.append({(leg2_x+1,leg2_y),(leg2_x,leg2_y)}) # 아래로 반시계방향 회전
    
    else: # 세로방향인 경우
        if board[leg1_x][leg1_y - 1] == 0 and board[leg2_x][leg2_y - 1] == 0: # 좌
            next_pos.append({(leg1_x,leg1_y-1),(leg1_x,leg1_y)}) # 왼쪽으로 반시계방향 회전
            next_pos.append({(leg2_x,leg1_y-1),(leg2_x,leg2_y)}) # 왼쪽으로 시계방향 회전
        if board[leg1_x][leg1_y + 1] == 0 and board[leg2_x][leg2_y + 1] == 0: # 우
            next_pos.append({(leg2_x,leg2_y),(leg2_x,leg2_y+1)}) # 오른쪽으로 시계방향 회전
            next_pos.append({(leg1_x,leg1_y),(leg1_x,leg1_y+1)}) # 오른쪽으로 반시계방향 회전
    return next_pos

def solution(board):
    start = {(1,1),(1,2)}
    visited = []
    q = deque()
    q.append((start, 0))
    while q: # bfs 수행
        now, cost = q.popleft()
        if (n,n) in now:
            return cost
        for next_pos in get_next_pos(now, board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

print(solution(board))
