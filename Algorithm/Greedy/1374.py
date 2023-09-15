import sys, math, heapq
input = sys.stdin.readline
INF = sys.maxsize


def sol():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        arr.append((b, c))
    arr.sort()
    q = []
    ans = 1
    for start, end in arr:
        while q and q[0] <= start:
            heapq.heappop(q)
        heapq.heappush(q, end)
        ans = max(ans, len(q))
    print(ans)


sol()
