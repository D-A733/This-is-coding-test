n, m = map(int, input().split())
# 맵 정보 입력받아 str으로 저장
ice = ['1' + input() + '1' for _ in range(n)]
# indexerror방지를 위해 둘레에 데이터 추가
ice.insert(0, '1'*(m+2))
ice.append('1'*(m+2))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(ice, x, y):
    # 현재 노드 방문 처리
    ice[x] =  ice[x][:y] + '1' + ice[x][y+1:]
    # 현재 노드 기준 상, 하, 좌, 우에 있는 노드 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 방문하지 않은 노드가 있으면 방문
        if ice[nx][ny] == "0":
            dfs(ice, nx, ny)
count = 0

for i in range(1, n+1):
        v = ice[i].find('0')
        # 각 행에서 '0'을 찾고 음료수 채우기
        while v != -1:
            dfs(ice, i, v)
            count += 1
            v = ice[i].find('0')

print(count)
