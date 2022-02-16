from collections import deque
import sys
import copy

read = sys.stdin.readline
n = int(read().rstrip())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
time = [0] * (n + 1)

for i in range(1, n+1):
    cost, *prior, end = map(int, read().split())
    indegree[i] = len(prior)
    time[i] = cost
    for k in prior:
        graph[k].append(i)

def Topology_sort():
    q = deque()
    result = copy.deepcopy(time)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

Topology_sort()
