import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global ground
    q = deque()
    q.append((x, y))
    ground[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if ground[nx][ny] == 1:
                    ground[nx][ny] = 0
                    q.append((nx, ny))


for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        ground[b][a] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

