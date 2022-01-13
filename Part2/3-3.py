n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
#각 행에서 최솟값를 뽑아 새로운 리스트를 만든다
min_value_card = [min(cards[i]) for i in range(n)]

#각 행에서 뽑은 최솟값들 중에 가장 큰 값을 선택한다.
result = max(min_value_card)
print(result)
