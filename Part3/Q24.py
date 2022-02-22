import sys
read = sys.stdin.readline
n = int(read())
data = list(map(int, read().split()))
data.sort()

print(data[(n - 1)// 2])
