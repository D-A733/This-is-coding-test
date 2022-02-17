s = input()
alpha = []
number = 0
for x in s:
    if x.isalpha():
        alpha.append(x)
    else:
        number += int(x)
alpha.sort()
print("".join(alpha) + str(number))
