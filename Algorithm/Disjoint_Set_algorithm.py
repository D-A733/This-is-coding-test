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

for _ in range(e):
    a, b = map(int, read().split())
    union_parent(parent, a, b)
    
print("각 원소가 속한 집합 : ", end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()
print("부모 테이블 : ", end='')
for i in range(1, v+1):
    print(parent[i], end=" " )
    
