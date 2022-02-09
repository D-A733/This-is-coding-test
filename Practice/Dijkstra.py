import sys
read = sys.stdin.readline
n, m, c = map(int, read().split())
inf = int(1e9)
distance = [inf] * (n+1)
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, read().split())
    graph[x].append((y,z))

def get_smallest_node():
    c = inf
    index = 0
    for i in range(1, n+1):
        if not visited[i] and c > distance[i]:
            c = distance[i]
            index = i
    return index

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
