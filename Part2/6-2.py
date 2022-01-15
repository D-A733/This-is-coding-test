n = int(input())
# 수를 입력받아 리스트에 저장
array = [input() for _ in range(n)]
# 내림차순 정렬 후 출
print(" ".join(sorted(array, reverse=True)))
