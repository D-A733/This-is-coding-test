from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    return bisect_right(array, right_value) - bisect_left(array, left_value)

# 사용 예시
array = [1, 1, 2, 4, 5, 5, 5, 6, 7 ,9 ,10]
right_value = 8
left_value = 3
print(count_by_range(array, left_value, right_value))

# 문자열개수 셀 때도 사용 가능
words = ['frodo', 'front', 'frost', 'frame', 'frier']
words.sort()
# fro??인 단어의 개수를 찾고 싶다면
print(count_by_range(words, 'froaa', 'frozz'))
