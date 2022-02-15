# 노드의 갯수가 5000개 이하일 경우 이용
# 시간복잡도 O(V^2) V:노드의 개수
import sys
read = sys.stdin.readline
# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, read().split())
# 시작 노드 입력받기
start = int(read())
visited = [False] * (n+1)
inf = int(1e9)
distance = [inf] * (n+1)

# 그래프 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b,c))

# 방문하지 않은 노드들 중에서 최단거리인 노드 구하는 함수
def get_smallest_node():
    min_value = inf
    index = 0
    for i in range(n+1):
        if not visited[i] and min_value >= distance[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해 초기값 설정
    distance[start] = 0
    visited[start] = True
    for b, c in graph[start]:
        distance[b] = c
    # 나머지 n-1개의 노드에 대해 반복
    for _ in range(n-1):
        # 최단거리인 노드를 구하고 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드에 연결된 다른 노드를 확인
        for b, c in graph[now]:
            # 현재 노드를 거쳐 가는게 더 짧은 경우
            if distance[b] >= c + distance[now]:
                distance[b] = c + distance[now]

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == inf:
        print("도달할 수 없습니다.")
    else:
        print("노드{} : {}".format(i, distance[i]))
    
