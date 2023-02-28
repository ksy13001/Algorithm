import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[]for _ in range(n + 1)]
value = [0] * (n + 1)

for i in range(1, n + 1):
    a = list(map(int, input().split()))
    value[i] = a[0]
    if len(a) > 2:
        indegree[i] += len(a[1:-1])
    else:
        dp[i] = value[i]
    for j in a[1:-1]:
        graph[j].append(i)


def sol():
    q = deque()
    ans = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        ans.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + value[i])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(dp[i])


sol()
