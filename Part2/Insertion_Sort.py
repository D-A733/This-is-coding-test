array = list(map(int, input().split()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # 자기보다 큰 수를 만나면 위치를 바꿈
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        # 자기보다 작은 수를 만나면 그자리에서 멈춤
        else:
            break        
print(array)
