def solution(s):
    n = len(s)
    answer = n
    
    for k in range(1, n//2 + 1):
        iter = 1
        memory = s[:k]
        compression = ""
        for i in range(k, n, k):
            try:
                if s[i:i+k] == memory:
                    iter += 1
                else:
                    compression += str(iter) + memory if iter >= 2 else memory
                    iter = 1
                    memory = s[i:i+k]
        compression += str(iter) + memory if iter >= 2 else memory
        answer = min(answer, len(compression))
    return answer

