from collections import deque
m, n = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
graph = []
tomato = deque()
for _ in range(n):
    graph.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            tomato.append((x, y))

while tomato:
    x, y = tomato.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            tomato.append((nx, ny))

t_on = 0
for i in range(n):
    if 0 in graph[i]:
        t_on =1
        break
if t_on == 0:
    print(max(map(max, graph))-1)
else:
    print(-1)
