import sys, heapq
input = sys.stdin.readline


def sol():
    n = int(input().rstrip())
    q = list(map(int, input().split()))
    heapq.heapify(q)
    ans = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += a + b
        heapq.heappush(q, (a+b))
    print(ans)


for _ in range(int(input())):
    sol()
