import copy
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global result
    g = copy.deepcopy(graph)
    zone = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == 0:
                    g[nx][ny] = 2
                    q.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                zone += 1
    result = max(result, zone)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    wall(cnt + 1)
                    graph[i][j] = 0


wall(0)
print(result)
