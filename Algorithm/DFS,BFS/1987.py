import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
ans = 0


def dfs(x, y, visited, cnt):
    global ans
    now = ord(graph[x][y]) - 65
    if visited[now]:
        if ans < cnt:
            ans = cnt
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[now]:
            visited[now] = True
            dfs(nx, ny, visited, cnt+1)
            visited[now] = False


if n == 1 and m == 1:
    print(1)
else:
    dfs(0, 0, [False for _ in range(26)], 0)
    print(ans)
