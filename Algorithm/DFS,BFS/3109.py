import sys
input = sys.stdin.readline


def dfs(x, y):
    global ans
    if y == m-1:
        return True
    for d in [(-1, 1), (0, 1), (1, 1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
            graph[nx][ny] = 'x'
            if dfs(nx, ny):
                return  True
    return False


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
ans = 0
for i in range(n):
    if dfs(i, 0):
        ans += 1
print(ans)
