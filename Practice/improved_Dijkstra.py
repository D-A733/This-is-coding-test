import heapq
import sys
inf = int(1e9)
read = sys.stdin.readline
n, m, c = map(int, read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, read().split())
    graph[x].append((y,z))
distance = [inf] * (n+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for y, z in graph[now]:
            cost = dist + z
            if cost < distance[y]:
                distance[y] = cost
                heapq.heappush(q, (cost, y))

dijkstra(c)
city = list(filter(lambda x: x < inf, distance))
print("{} {}".format(len(city) - 1, max(city)))
