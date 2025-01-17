def solution(cap, n, deliveries, pickups):
    answer = 0
    for i in range(n - 1, -1, -1):

        now = max(deliveries[i], pickups[i], 0)
        cnt, mod = now // cap, now % cap
        cnt = cnt + 1 if mod > 0 else cnt
        answer += (i + 1) * cnt * 2 

        if i > 0:
            deliveries[i - 1] -= abs(deliveries[i] - cap * cnt)
            pickups[i - 1] -= abs(pickups[i] - cap * cnt)

    return answer

print(solution( 1, 5, [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]))
