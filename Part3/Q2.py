number = list(map(int, list(input())))
result = number[0]
for i in number[1:]:
    if result + i > result*i:
        result += i
    else:
        result *= i

print(result)
