import sys
read = sys.stdin.readline

n = int(read())
data = [list(read().split()) for _ in range(n)]

data.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(n):
    print(data[i][0])
