from collections import deque
import sys

read = sys.stdin.readline

v, e = map(int, read().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, read().split())
    graph[a].append(b)
    indegree[b] += 1

def Topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

Topology_sort()
