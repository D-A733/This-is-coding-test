S = input()
zero = S.split("1")
one = S.split("0")
result = min(len(zero) - zero.count(''), len(one) - one.count(''))
print(result)
