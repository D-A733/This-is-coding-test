import sys
read = sys.stdin.readline

n = 5
stages = [2,1,2,6,2,4,3,3]

def solution(N, stages):
    result = []
    length = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        result.append((fail,i))
        length -= count
    result.sort(key=lambda x:(-x[0],x[1]))
    answer = [x[1] for x in result]
    return answer

print(solution(n, stages))
