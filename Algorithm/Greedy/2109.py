import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = []
    ans = 0
    md = 0
    for _ in range(n):
        p, d = map(int, input().split())    # d 일 까지 오면 p 만큼 돈
        md = max(md, d)
        heapq.heappush(arr, (-p, d))
    schedule = [0] * (md+1)
    while arr:
        pay, date = heapq.heappop(arr)
        while schedule[date] != 0 and date > 1:
            date -= 1
        if schedule[date] == 0:
            ans += pay
            schedule[date] = pay
    print(-ans)


sol()
