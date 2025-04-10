import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    dp[b] += 1


def sol():
    ans = []
    q = []
    for i in range(1, n+1):
        if dp[i] == 0:
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        ans.append(now)
        for i in graph[now]:
            dp[i] -= 1
            if dp[i] == 0:
                heapq.heappush(q, i)
    print(*ans)


sol()
