n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],
               [2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def check(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥인 경우
            # 바닥위에 있거나 다른 기둥 위에 있거나 보의 한쪽 끝부분에 있는 경우 통과
            if y == 0 or [x, y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            else: # 아니면 불가능한 경우
                return False
        else: # 보인 경우
            # 한쪽 끝부분이 기둥 위에 있거나 양쪽 끝부분이 다른 보와 동시에 연결된 경우 통과
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else: # 아니면 불가능한 경우
                return False
    return True

answer = []
for x, y, a, b in build_frame:
    if b == 0: # 삭제
        answer.remove([x,y,a]) # 일단 삭제
        if not check(answer): # 문제가 있으면 다시설치
            answer.append([x,y,a]) 
    else: # 설치
        answer.append([x,y,a]) # 일단 설치
        if not check(answer): # 문제가 있으면 다시삭제
            answer.remove([x,y,a])
        
print(sorted(answer))
