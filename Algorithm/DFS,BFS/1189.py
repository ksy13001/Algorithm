import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, cnt):
    global ans
    if x == 0 and y == m-1:
        if cnt == k:
            ans += 1
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                graph[nx][ny] = 'F'
                dfs(nx, ny, cnt + 1)
                graph[nx][ny] = '.'


n, m, k = map(int, input().split())
ans = 0
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
graph[n-1][0] = 'F'
dfs(n-1, 0, 1)
print(ans)
