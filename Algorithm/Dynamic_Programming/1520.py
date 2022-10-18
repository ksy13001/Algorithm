import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dp = [[-1 for _ in range(m)] for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))
