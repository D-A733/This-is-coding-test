n, m = map(int, input().split())
weight = list(map(int, input().split()))
count = [0] * 11
for x in weight:
    count[x] += 1

result = 0
for i in range(n):
    result += n - count[weight[i]]

print(result // 2)
