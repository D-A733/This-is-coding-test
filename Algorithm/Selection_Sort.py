# 시간복잡도 O(N^2)
array = list(map(int, input().split()))

for i in range(len(array)-1):
    min_index = i
    # 차례대로 비교하여 가장 작은 수의 인덱스 조사
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    # 가장 작은수가 i번째 자리에 오게 바꿈
    array[i], array[min_index] = array[min_index], array[i]
print(array)
