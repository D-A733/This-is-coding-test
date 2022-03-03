import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

