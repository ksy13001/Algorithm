import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
friend = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)


def bfs(start):
    cnt = 0
    distance = [0]*(n+1)
    q = deque()
    q.append((start, cnt))
    distance[start] = -1
    while q:
        now, cnt = q.popleft()
        for next_f in friend[now]:
            if distance[next_f] == 0:
                distance[next_f] = cnt + 1
                q.append((next_f, cnt + 1))
    return sum(distance)


result = [INF]*(n+1)
for i in range(1, n+1):
    result[i] = bfs(i)
print(result.index(min(result)))
