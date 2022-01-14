def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 왼쪽부터 pivot보다 큰 값 찾음
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽부터 pivot보다 작은 값 찾음
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈린 경우 right와 pivot을 바꿈
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않은 경우 left와 right를 바꿈
        else:
            array[left], array[right] = array[right], array[left]
    # 분할된 왼쪽 부분과 오른쪽 부분에 대하여 각각 정렬실행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

array = list(map(int, input().split()))
quick_sort(array, 0, len(array) - 1)
print(array)
    
