column = "0abcdefgh"
coordinate = input()
# 입력받은 좌표를 정수좌표로 변환
x = column.index(coordinate[0])
y = int(coordinate[1])

# 이동가능한 경로들의 좌표이동
dx = [-2, -2, -1, 1, -1, 1, 2, 2]
dy = [1, -1, 2, 2, -2, -2, 1, -1]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    # 이동 후 좌표가 정원 밖으로 나간다면 경우의 수에 추가하지 않음
    if nx < 1 or nx > 8 or ny < 1 or ny >8:
        continue
    count += 1
print(count)
