import sys
from collections import deque
input = sys.stdin.readline
t = int(input())


def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1 for _ in range(n+1)]
    visited[start] = time[start]
    while q:
        now = q.popleft()
        for i in graph[now]:
            a = visited[now] + time[i]
            if visited[i] == -1 or visited[i] < a:
                q.append(i)
                visited[i] = a
    return max(visited)


for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[]for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b].append(a)
    w = int(input())
    print(bfs(w))
