def quick_sort(array, start, end):
    if start <= end:
        return
    left = start
    right = end
    pivot = start
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[right] >= array[pivot]:
            right -= 1
        if left < right: # 안 엇갈린 경우
            array[left], array[right] = array[right], array[left]
        else: # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

