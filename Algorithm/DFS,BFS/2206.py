from collections import deque
INF = int(1e9)
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


def bfs(x, y, broke):
    global visited
    q = deque()
    q.append((x, y, broke))
    while q:
        x, y, broke = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][broke]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][broke] == 0:
                    visited[nx][ny][broke] = visited[x][y][broke] + 1
                    q.append((nx, ny, broke))
                elif graph[nx][ny] == 1 and broke == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
    return -1
print(bfs(0, 0, 0))
