import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1


def bfs(sx, sy):
    q = deque([(sx, sy, 1)])
    visited[sx][sy] = True
    route = 1
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
                route += 1
    return route


ans = 0
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(ans, bfs(i, j))
print(ans)
