from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, 1, -1, -1, 1]


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True




while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    visited = [[False for _ in range(m)]for _ in range(n)]
    cnt = 0
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i, j, visited)
                cnt += 1
    print(cnt)
