import sys
inf = int(1e9)
read = sys.stdin.readline
n, m, c = map(int, read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, read().split())
    graph[x].append((y,z))

distance = [inf] * (n+1)
visited = [False] * (n+1)

def get_smallest_node():
    dist = inf
    index = 0
    for i in range(n-1):
        if not visited[i] and distance[i] < dist:
            dist = distance[i]
            index = i
    return i

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for y, z in graph[start]:
        distance[y] = z
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for y, z in graph[now]:
            dist = distance[now] + z
            if dist < distance[y]:
                distance[y] = dist

dijkstra(c)

city = list(filter(lambda x: x < inf, distance))
print("{} {}".format(len(city) - 1, max(city)))
