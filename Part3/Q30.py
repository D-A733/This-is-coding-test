from bisect import bisect_left, bisect_right

words = ['frodo','front','frost','frozen','frame','kakao']
queries = ['fro??','????o','fr???','fro???','pro?']

def count_by_range(array, left_value, right_value):
    return bisect_right(array, right_value) - bisect_left(array, left_value)

def solution(words, queries):
    word = [[] for _ in range(10001)]
    reverse_word = [[] for _ in range(10001)]
    answer = []
    for x in words:
        word[len(x)].append(x)
        reverse_word[len(x)].append(x[::-1])

    for i in range(1, 10001):
        word[i] = sorted(word[i])
        reverse_word[i] = sorted(reverse_word[i])

    for query in queries:
        n = len(query)
        if query[-1] == "?": # 접미사에 ?가 있는 경우
            count = count_by_range(word[n], query.replace("?", "a"), query.replace("?", "z"))
        else: # 접두사에 ?가 있는 경우
            query = query[::-1]
            count = count_by_range(reverse_word[n], query.replace("?", "a"), query.replace("?", "z"))
        answer.append(count)

    return answer


print(solution(words, queries))
