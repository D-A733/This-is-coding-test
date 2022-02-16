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

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    command, a, b = map(int, read().split())
    if command:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parent, a, b)
