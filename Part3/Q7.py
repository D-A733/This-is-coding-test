n = input()
left = n[:len(n) // 2]
right = n[len(n) // 2:]
if sum(list(map(int, list(left)))) == sum(list(map(int, list(right)))):
    print("LUCKY")
else:
    print("READY")
