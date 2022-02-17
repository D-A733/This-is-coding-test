import heapq
def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    rotate = 0
    while q:
        time, now = heapq.heappop(q)
        if k >= (time - rotate) * (len(q) + 1):
            k -= (time - rotate) * (len(q) + 1)
            rotate = time
        else:
            heapq.heappush(q, (time, now))
            break
    
    result = sorted(q, key=lambda x: x[1])
    answer = result[k % (len(q) + 1)][1]
    
    return answer
