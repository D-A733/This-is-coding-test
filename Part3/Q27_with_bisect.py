from bisect import bisect_left, bisect_right
import sys
read = sys.stdin.readline
n, x = map(int, read().split())
data = list(map(int, read().split()))

left_index = bisect_left(data, x)
right_index = bisect_right(data, x)
if left_index >= n:
    print(-1)
else:
    print(right_index - left_index)
