from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(sx, sy, k):
    global ans
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1
    over = False
    while q:
        x, y = q.popleft()
        if x == 0 or x == n-1 or y == 0 or y == m-1:
            over = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] <= k:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
    if not over:
        ans += cnt


n, m = map(int, input().split())
graph = []
ans = 0
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

for k in range(1, 9):
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] <= k:
                bfs(i, j, k)
print(ans)
