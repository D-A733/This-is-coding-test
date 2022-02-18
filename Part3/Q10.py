import copy

def rotate_a_matrix_by_90_degree(key):
    n = len(key)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = key[i][j]
    return result

def check(test_lock):
    n = len(test_lock)//3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if test_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    total_lock = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            total_lock[i+n][j+n] = lock[i][j]
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for i in range(n - m + 1, 2*n):
            for j in range(n - m + 1, 2*n):
                test_lock = copy.deepcopy(total_lock)
                for x in range(m):
                    for y in range(m):
                        test_lock[i+x][j+y] += key[x][y]
                if check(test_lock):
                    return True
    return False
