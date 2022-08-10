import sys

n = int(input())
graph = []
max_area = 0
max_num = 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    max_num = max(max(a), max_num)
    graph.append(a)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sys.setrecursionlimit(10 ** 6)


def dfs(height, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if graph[nx][ny] > height:
                visited[nx][ny] = 1
                dfs(height, nx, ny)


for h in range(max_num):
    visited = [[0]*n for _ in range(n)]
    area = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                area += 1
                visited[i][j] = 1
                dfs(h, i, j)
    max_area = max(area, max_area)
print(max_area)
