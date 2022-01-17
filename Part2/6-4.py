import sys
read = sys.stdin.readline
# 정보 입력 받기
n, k = map(int, read().split())
A = list(map(int, read().split()))
B = list(map(int, read().split()))
# A는 오름차순으로, B는 내림차순으로 정렬
A.sort()
B.sort(reverse=True)
# 최대 K번 반복
for i in range(k):
    min_A, max_B = A[i], B[i]
    # 첫번째부터 A와 B원소 크기를 비교하여 B의 원소가 더 크면 바꾸기
    if min_A <= max_B:
        A[i] = max_B
    # A의 원소가 더 크면 더 이상 바꿀 필요가 없으니 반복문 탈출
    else:
        break
print(sum(A))
