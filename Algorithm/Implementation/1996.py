n = int(input())
dx = [1, -1, 1, 0, -1, 0, 1, -1]
dy = [1, -1, 0, 1, 0, -1, -1, 1]
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[0 for _ in range(n)]for _ in range(n)]


def install(x, y):
    visited[x][y] = '*'
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 'M' and visited[nx][ny] != '*':
            if visited[nx][ny] + int(graph[x][y]) < 10:
                visited[nx][ny] += int(graph[x][y])
            else:
                visited[nx][ny] = 'M'


for i in range(n):
    for j in range(n):
        if graph[i][j] != '.':
            install(i, j)
for i in range(n):
    print(''.join(map(str, visited[i])))
