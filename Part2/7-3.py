import sys
# 높이 h로 잘랐을 때 나오는 떡의 양을 구하는 함수 정의
def length(rice, h):
    sliced_rice = [x for x in rice if x > h]
    return sum(sliced_rice) - h * len(sliced_rice)
# 이진탐색 함수 정의
def binary_search(target, start, end):
    # 타겟값을 찾지 못했을 경우
    if start > end:
        # end의 높이로 잘랐을 때 타겟값보다 큰 경우
        if length(rice, end) > target:
            return end
        # end의 높이로 잘랐을 때 타겟값보다 작은 경우
        else:
            return end + 1
    mid = (start + end) // 2
    # 중간값이 타겟값일 경우 중간값 반환
    if length(rice, mid) == target:
        return mid
    # 중간값이 타겟값보다 큰 경우 오른쪽부분에 대해서 탐색 반복
    elif length(rice, mid) > target:
        return binary_search(target, mid + 1, end)
    # 중간값이 타겟값보다 작은 경우 왼쪽부분에 대해서 탐색 반복
    else:
        return binary_search(target, start, mid - 1)

# 정보 입력 받기
read = sys.stdin.readline
n, m = map(int, read().split())
rice = list(map(int, read().split()))
result = binary_search(m, 0, max(rice))
print(result)
