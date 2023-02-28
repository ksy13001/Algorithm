from collections import deque
import sys
input = sys.stdin.readline
t = int(input())


def sol():
    q = deque()
    result = []
    cnt = 1
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, cnt))
            dp[i].append(cnt)
    while q:
        now, n_cnt = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            dp[i].append(n_cnt)
            if indegree[i] == 0:
                if dp[i].count(n_cnt) > 1:
                    q.append((i, n_cnt + 1))
                else:
                    q.append((i, n_cnt))
    if dp[n].count(max(dp[n])) > 1:
        print(max(dp[n]) + 1)
    else:
        print(max(dp[n]))


for _ in range(t):
    k, n, p = map(int, input().split())
    dp = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    graph = [[]for _ in range(n + 1)]
    for i in range(1, p + 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    print(k, end=' ')
    sol()
