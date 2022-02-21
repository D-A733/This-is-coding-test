from collections import deque
import sys

read = sys.stdin.readline
n, m, k, start = map(int, read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

min_distance = [-1] * (n+1)

q = deque([start])
min_distance[start] = 0
while q:
    now = q.popleft()
    for i in graph[now]:
        if min_distance[i] == -1:
            q.append(i)
            min_distance[i] = min_distance[now] + 1

check = False

for i in range(1, n+1):
    if min_distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
