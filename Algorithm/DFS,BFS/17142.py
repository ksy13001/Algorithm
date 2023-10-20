import sys
from collections import deque
from itertools import combinations
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
virus = []
blank = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            blank = True
if blank:
    k = list(combinations(virus, m))


    def bfs(q):
        visited = [[0 for _ in range(n)]for _ in range(n)]
        for x, y in q:
            visited[x][y] = 1
        temp = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    if graph[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        temp = max(temp, visited[nx][ny])
                    if graph[nx][ny] == 2:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0 and graph[i][j] == 0:
                    return INF
        return temp

    ans = INF
    for i in range(len(k)):
        q = deque(k[i])
        ans = min(ans, bfs(q))
    if ans >= INF:
        print(-1)
    else:
        print(ans-1)
else:
    print(0)
