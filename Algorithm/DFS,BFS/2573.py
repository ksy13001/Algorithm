import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] <= 0:
                nz[x][y] += 1
            if 1 <= nx < n-1 and 1 <= ny < m-1 and not visited[nx][ny] and graph[nx][ny] > 0:
                q.append((nx, ny))
                visited[nx][ny] = True


ans = 0
cnt = 0
while cnt < 2:
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    nz = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and graph[i][j] > 0:
                cnt += 1
                if cnt <= 1:
                    bfs(i, j)
    if cnt > 1:
        print(ans)
        break
    elif cnt == 0:
        print(0)
        break
    else:
        ans += 1
    for i in range(n):
        for j in range(m):
            graph[i][j] -= nz[i][j]

