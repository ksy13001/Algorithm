import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]for i in range(n+1)]
dp = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    dp[b] += 1


def sol():
    ans = []
    q = deque()
    for i in range(1, n+1):
        if dp[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        ans.append(now)
        for i in graph[now]:
            dp[i] -= 1
            if dp[i] == 0:
                q.append(i)

    for i in ans:
        print(i, end=' ')

        
sol()
