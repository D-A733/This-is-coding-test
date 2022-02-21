from itertools import combinations
import sys
read = sys.stdin.readline

n, m = map(int, read().split())

city = []
for _ in range(n):
    city.append(list(map(int, read().split())))

# 집, 치킨집이 있는 좌표 정보
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
h = len(house)
c = len(chicken)

def total_chicken_distance(house, chicken):
    result = 0
    for x, y in house:
        min_dist = 100
        for a, b in chicken:
            min_dist = min(min_dist, abs(x-a) + abs(y-b))
        result += min_dist
    return result

# m개의 치킨집을 고르는 모든 경우
candidates = list(combinations(chicken, m))
city_chicken_distance = 10000

# 모든 경우에 대해 치킨거리 계산
for candidate in candidates:
    city_chicken_distance = min(city_chicken_distance, total_chicken_distance(house,candidate))

print(city_chicken_distance)
