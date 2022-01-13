n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
result, i = 0, 0

#리스트에서 가장 큰 값과 두번째로 가장 큰 값 저장
max_value = max(num_list)
second_num_list = num_list
second_num_list.remove(max_value)
second_max_value = max(second_num_list)

#가장 큰 값을 K번 더한 다음에는 두번째로 큰 값을 더함
for _ in range(m):
    if i == k:
        i = 0
        result += second_max_value
    else:
        i += 1
        result += max_value
        
print(result)
