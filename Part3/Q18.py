from collections import deque
def check_right(p):
    q = deque()
    for bracket in p:
        if bracket == "(":
            q.append(bracket)
        else:
            if len(q) == 0:
                return False
            else:
                q.pop()
    return True

def divide(p):
    count_open = 0
    count_close = 0
    u = ""
    for i in range(len(p)):
        if p[i] == "(":
            count_open += 1
        else:
            count_close += 1
        u += p[i]
        if count_open == count_close:
            index = i
            break
    v = p[i+1:]
    return u, v

def solution(p):
    if not p or check_right(p):
        return p
    u, v = divide(p)
    if check_right(u):
        return u + solution(v)
    else:
        new_u = ''
        for bracket in u[1:-1]:
            new_u += ")" if bracket == "(" else "("
        return "(" + solution(v) + ")" + new_u
    
p = input()
print(solution(p))
