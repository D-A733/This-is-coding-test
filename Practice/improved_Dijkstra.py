import heapq
import sys
read = sys.stdin.readline
n, m, start = map(int, read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b,c))

inf = int(1e9)
distance = [inf] * (n+1)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
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
city = list(filter(lambda x: x < inf, distance))
print("{} {}".format(len(city) - 1, max(city)))
