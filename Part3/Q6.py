# 50점 답안. 효율성이 부
def solution(food_times, k):
    if (k+1) > sum(food_times):
        return -1
    m = max(food_times)
    n = len(food_times)
    count = [0] * (m + 1)
    for x in food_times:
        count[x] += 1
        
    for i in range(1, m+1):
        if k >= n:
            k -= n
        else:
            number = i
            break
        n = n - count[i]

    for i in range(len(food_times)):
        if number <= food_times[i] and k >= 0:
            answer = i + 1
            k -= 1
    return answer

food_times = [3, 1, 2]
k = 5
answer = solution(food_times, k)
