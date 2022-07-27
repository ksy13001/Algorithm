import sys
import copy

n, m = map(int, sys.stdin.readline().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def spread(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                spread(nx, ny)


def get_safe(g):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                cnt += 1
    return cnt


def dfs(wall_cnt):
    global result
    print('-'*40)
    if wall_cnt == 3:
        after_graph = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if after_graph[i][j] == 2:
                    spread(i, j)
        result = max(result, get_safe(after_graph))
        return
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    wall_cnt += 1
                    dfs(wall_cnt)
                    graph[i][j] = 0
                    wall_cnt -= 1


dfs(0)
print(result)
