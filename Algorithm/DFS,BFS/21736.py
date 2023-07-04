from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited = [[False for _ in range(m)]for _ in range(n)]
    visited[sx][sy] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 'X':
                q.append((nx, ny))
                visited[nx][ny] = True
                if graph[nx][ny] == 'P':
                    print(nx, ny)
                    cnt += 1
    if cnt > 0:
        return cnt
    else:
        return 'TT'

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            print(bfs(i, j))21736.py
