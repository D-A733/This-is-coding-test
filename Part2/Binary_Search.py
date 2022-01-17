def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 타겟이 중간값보다 작은경우 왼쪽 확인
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 타겟이 중간값보다 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    # 타겟이 중간값이면 중간값 반환
    else:
        return mid
# 정보 입력 받기    
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1, "번째")
