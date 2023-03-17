import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, now):
    visited[x][y] = True
    if graph[x][y] == 'R':
        graph[x][y] = 'G'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and now == graph[nx][ny]:
            dfs(nx, ny, now)



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
            dfs(i, j, graph[i][j])
            ans1 += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            ans2 += 1
print(ans1, ans2)
