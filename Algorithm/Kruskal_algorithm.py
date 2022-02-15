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
v, e = map(int, read().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, read().split())
    edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        print(a, b, cost, sep=',')

print(result)
