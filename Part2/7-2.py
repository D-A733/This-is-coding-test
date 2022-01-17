import sys
# 이진 탐색 함수 정의
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 중간값이 타겟값이라면 중간값 반환
        if array[mid] == target:
            return mid
        # 중간값이 타겟값보다 크다면 왼쪽 부분에 대해서 반복
        elif array[mid] > target:
            end = mid - 1
        # 중간값이 타겟값보다 작다면 오른쪽 부분에 대해서 반복
        else:
            start = mid + 1
    # 못찾았으면 None 반환
    return None
# 정보 입력 받기
read = sys.stdin.readline
n = int(read())
array = list(map(int, read().split()))
m = int(read())
ask = list(map(int, read().split()))
# 이진탐색을 활용하기 위해 array를 오름차순 정렬
array.sort()
# 요청한 부품 번호를 하나씩 이진탐색으로 확인
for i in ask:
    result = binary_search(array, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
