import sys
read = sys.stdin.readline

n, c = map(int, read().split())
array = [int(read()) for _ in range(n)]
array.sort()

def bisect_search(array, start_gap, end_gap, c):
    result = 0
    while start_gap <= end_gap:
        mid_gap = (start_gap + end_gap) // 2
        if count_c(array, mid_gap) >= c: # c개 이상 공유기 설치가 가능하면 gap을 늘리기
            start_gap = mid_gap + 1
            result = mid_gap
        else: # c개 미만 공유기 설치가 가능하면 gap 줄이기
            end_gap = mid_gap - 1
    return result

# 첫번째 원소부터 시작해 인접한 원소가 gap이상 떨어져 있는 원소의 총 개수
def count_c(array, gap):
    count = 1
    previous = 0
    n = len(array)
    for i in range(1, n):
        if array[previous] + gap <= array[i]:
            count += 1
            previous = i
    return count

print(bisect_search(array, 1, array[-1] - array[0], c))
