from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
city = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    city[a].append(b)
distance = [-1]*(n+1)
result = 0
ex = 0


def bfs(v):
    que = deque()
    que.append(v)
    distance[v] = 0
    while que:
        now = que.popleft()
        for i in city[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                que.append(i)


bfs(x)
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        ex = 1
if ex == 0:
    print(-1)
