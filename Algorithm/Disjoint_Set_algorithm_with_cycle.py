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
cycle = False

for _ in range(e):
    x, y = map(int, read().split())
    if find_parent(parent, x) == find_parent(parent, y):
        cycle = True
        break
    else:
        union_parent(parent, x, y)

if cycle:
    print("싸이클이 발생했습니다.")
else:
    for i in range(1, v+1):
        print(find_parent(parent, i), end=' ')
