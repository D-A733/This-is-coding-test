import sys
read = sys.stdin.readline

n, x = map(int, read().split())
array = list(map(int, read().split()))

def count_x(array, n, x):
    start = 0
    end = n - 1

    a = first(array, start, end, x)
    b = last(array, start, end, x)
    if not first(array, start, end, x):
        return -1
    return b - a + 1

def first(array, start, end, x):
    if start > end:
        return False
    mid = (start + end) // 2
    
    if (mid == 0 or array[mid - 1] < x) and array[mid] == x:
        return mid
    
    elif array[mid] >= x:
        return first(array, start, mid - 1, x)
    
    else:
        return first(array, mid + 1, end, x)

def last(array, start, end, x):
    if start > end:
        return False
    mid = (start + end) // 2

    if (mid == n - 1 or array[mid + 1] > x) and array[mid] == x:
        return mid

    elif array[mid] <= x:
        return last(array, mid + 1, end, x)
    
    else:
        return last(array, start, mid - 1, x)

print(count_x(array, n, x))
