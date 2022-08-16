def solution(N, stages):
    answer = []
    stage = sorted(stages)
    n = len(stage)
    for i in range(1, N+1):
        a = stage.count(i)
        if a == 0:
            fail = 0
        else:
            fail = a/n
        answer.append((i, fail))
        n -= a
    answer.sort(key=lambda x: -x[1])
    answer = [i[0] for i in answer]
    return answer
