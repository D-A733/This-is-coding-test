n, k = map(int, input().split())
count = 0

# n이 1이 될 때까지 반복
while n != 1:
    r = n % k
    
    # n이 k로 나누어 떨어지면 우선 나누기
    if r == 0:
        n //= k
        count += 1
    else:
        # n > k일 경우 -1을 r번 반복해서 n을 k의 배수로 만들기
        if n > k:
            count += r
            n -= r
            
        # n < k일 경우 -1을 r-1번 반복해서 n을 1로 만들기
        else:
            count += r-1
            n -= r-1
print(count)
