import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, st):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if st == 'ori':
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny, 'ori')
        else:
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[x][y] == 'G' or graph[x][y] == 'R':
                    if graph[nx][ny] != 'B':
                        dfs(nx, ny, 'rg')
                else:
                    if graph[nx][ny] == graph[x][y]:
                        dfs(nx, ny, 'rg')


n = int(input())
graph = []
ans1 = 0
ans2 = 0
for _ in range(n):
    graph.append(list(input().strip()))
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 'ori')
            ans1 += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 'rg')
            ans2 += 1
print(ans1, ans2)
