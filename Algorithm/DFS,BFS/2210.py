import sys
sys.setrecursionlimit(10**6)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
graph = []
for _ in range(5):
    graph.append(list(map(str, input().split())))
num = []


def dfs(x, y, now):
    if len(now) == 6:
        if now not in num:
            num.append(now)
        now = ''
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, now + graph[nx][ny])
    return


for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(num))


