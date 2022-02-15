# 시간복잡도 O(N + K), K는 값이 가장 큰 데이터
array = list(map(int, input().split()))
count = [0] * (max(array) + 1)
for i in array:
    count[i] += 1

for i in range(len(count)):
    print("{} : {}".format(i, count[i]))
