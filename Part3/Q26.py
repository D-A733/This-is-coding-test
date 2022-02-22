import heapq

n = int(input())
q = []
for i in range(n):
    data = int(input())
    heapq.heappush(q, data)
result = 0
for _ in range(n-1):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a+b)
    result += (a+b)

print(result)
