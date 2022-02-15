# 노드가 10,000개가 넘어간다면 향상된 다익스트라를 이용
# 시간복잡도 O(ElogV) E:간선의 개수, V:노드의 개수
import heapq
import sys
read = sys.stdin.readline

# 노드와 간선의 개수 입력받기
n, m = map(int, read().split())

# 시작 노드 입력받기
start = int(read())
inf = int(1e9)

# 최단거리값 초기화
distance = [inf] * (n + 1)

# 그래프 정보 입력받기
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    # 힙이 빌때까지 반복
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <= dist:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

dijkstra(start)

for i in range(1, n+1):
    print(distance[i])
