from itertools import permutations
import sys
read = sys.stdin.readline

n = int(read())
sequence = list(map(int, read().split()))

# +, -, *, / 개수
data = list(map(int, read().split()))

operators = []
for i in range(4):
    operators += [i] * data[i] 

max_value = -int(1e9)
min_value = int(1e9)
repeat = []
# 모든 사칙연산 경우의 수
for candidate in list(set(permutations(operators, n-1))):
    repeat.append(candidate)
    result = sequence[0]
    for i in range(n-1):
        if candidate[i] == 0: # +
            result += sequence[i+1]
        elif candidate[i] == 1: # -
            result -= sequence[i+1]
        elif candidate[i] == 2: # *
            result *= sequence[i+1]
        else: # %
            if result < 0: # 음수를 나누는 경우
                result = -(abs(result) // sequence[i+1])
            else: # 양수를 나누는 경우
                result //= sequence[i+1]
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
