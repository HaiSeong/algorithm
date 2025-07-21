def solution(N, stages):
    # 1, 2, 2, 2, 3, 3, 4, 6

    visiting = len(stages)
    rates = []
    for level in range(1, N + 1):
        challenging = stages.count(level)

        if visiting == 0:
            rate = 0
        else:
            rate = challenging / visiting
        rates.append((rate, level))

        visiting -= challenging

    rates.sort(key=lambda x: -x[0])
    return list(map(lambda x: x[1], rates))

