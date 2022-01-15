n = int(input())
# 이름과 점수를 튜플로 묶어서 리스트에 저장
data = [tuple(input().split()) for _ in range(n)]

# 점수를 기준으로 오름차순 정렬
data.sort(key=lambda x:int(x[1]))
for i in data:
    print(i[0], end=" ")
