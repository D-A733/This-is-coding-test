import sys
import heapq
read = sys.stdin.readline
# 도시, 통로의 개수, 시작도시 입력받기
n, m, start = map(int, read().split())
# 그래프 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b,c))

inf = int(1e9)
distance = [inf] * (n+1)

# dijkstra 알고리즘 수행
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if distance[b] > cost:
                distance[b] = cost
            heapq.heappush(q, (cost, b))

dijkstra(start)
# 도달가능한 도시만 고르기
city = list(filter(lambda x: x < inf, distance))
print("{} {}".format(len(city)-1, max(city)))
