import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, 1, -1, -1, 1]


def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    cnt = 0
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
