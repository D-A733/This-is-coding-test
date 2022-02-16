import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

read = sys.stdin.readline
n, m = map(int, read().split())

parent = [0] * (n + 1)
for i in range(1, n+1):
    parent[i] = i

edges = []
result = 0
max_cost = 0

for _ in range(m):
    a, b, cost = map(int, read().split())
    edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # 제일 마지막에 고른 간선이 비용이 가장 큰 간선
        max_cost = cost

# 최소신장트리에서 간선 하나만 빼면 분리된 두개의 최소신장트리가 생긴다.
total_result = result - max_cost
print(total_result)

