n = int(input())
fearness = list(map(int, input().split()))

result, rest = 0, 0
for i in range(1, n+1):
    a = fearness.count(i)
    result += a//i
    rest += a%i
    if rest >= i:
        result += 1
        rest -= 1

print(result)
