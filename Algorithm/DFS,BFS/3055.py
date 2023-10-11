import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            q.append((i, j, 'w'))
        if graph[i][j] == 'S':
            sx, sy = i, j
q.append((sx, sy, 's'))
ans = 'KAKTUS'


def bfs():
    global ans
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        x, y, mode = q.popleft()
        #print('now :', x, y, q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '.':
                    if visited[nx][ny] == 0:
                        # 물먼저
                        if mode == 'w':
                            visited[nx][ny] = visited[x][y] - 1
                            q.append((nx, ny, 'w'))
                        else:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny, 's'))
                if graph[nx][ny] == 'D' and mode == 's' and visited[x][y] >= 0:
                    ans = visited[x][y] + 1
                    return
#for i in range(n): print(visited[i])
bfs()
print(ans)
