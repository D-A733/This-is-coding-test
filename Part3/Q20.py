from itertools import combinations
import sys
read = sys.stdin.readline
n = int(read())
graph = [list(read().split()) for _ in range(n)]

student = []
teacher = []
blank = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            student.append((i,j))
        elif graph[i][j] == 'T':
            teacher.append((i,j))
        else:
            blank.append((i,j))
            
def check(teacher, student, stuff): # 감시를 피할 수 있는지 체크
    # 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for x, y in teacher:
        for i in range(4):
            for k in range(1, n):
                nx = x + dx[i]*k
                ny = y + dy[i]*k
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                    continue
                if (nx,ny) in stuff:
                    break
                if (nx,ny) in student:
                    return False
    return True

def solution(teacher, student, blank):
    for stuff in list(combinations(blank, 3)):
        if check(teacher, student, stuff):
            return "YES"
    return "NO"

print(solution(teacher, student, blank))
