import bisect

def count(query, words):
    pivot1 = query.replace('?', 'a')
    pivot2 = query.replace('?', 'z')

    start = bisect.bisect_left(words, pivot1)
    end = bisect.bisect_right(words, pivot2)
    return end - start


def set_words_dict(words, queries):
    lengths = set(list(map(len, words)) + list(map(len, queries)))
    words_map = {length: [] for length in lengths}
    reversed_words_map = {length: [] for length in lengths}

    for word in words:
        words_map[len(word)].append(word)
        reversed_words_map[len(word)].append(word[::-1])

    for length in words_map:
        words_map[length].sort()
    for length in reversed_words_map:
        reversed_words_map[length].sort()

    return words_map, reversed_words_map


def solution(words, queries):
    words_map, reversed_words_map = set_words_dict(words, queries)

    answer = []
    for query in queries:
        words, reversed_words = words_map[len(query)], reversed_words_map[len(query)]
        if query[0] == '?':
            reversed_query = query[::-1]
            answer.append(count(reversed_query, reversed_words))
        else:
            answer.append(count(query, words))
    return answer
