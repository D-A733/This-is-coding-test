import sys
read = sys.stdin.readline

n = int(read())
array = list(map(int, read().split()))

def bisect_search(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return bisect_search(array, mid + 1, end)
    else:
        return bisect_search(array, start, mid - 1)

print(bisect_search(array, 0, n-1))
