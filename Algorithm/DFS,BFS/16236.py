from collections import deque
n = int(input())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for _ in range(n):
    graph.append(list(map(int, input().split())))
eat = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx = i
            sy = j
        elif 0 < graph[i][j] < 9:
            eat.append((i, j, graph[i][j]))
graph[sx][sy] = 0
s_eat = 0
s_size = 2
time = 0


def search(x, y):
    visited = [[False for _ in range(n)]for _ in range(n)]
    q = deque()
    t = 0
    q.append((x, y, t))
    visited[x][y] = True
    fish = []
    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if graph[nx][ny] == s_size or graph[nx][ny] == 0:
                        q.append((nx, ny, t + 1))
                        visited[nx][ny] = True
                    elif 0 < graph[nx][ny] < s_size:
                        fish.append((nx, ny, t + 1))
    fish.sort(key=lambda x: (-x[2], -x[0], -x[1]))
    return fish


while True:
    fish = search(sx, sy)
    if len(fish) == 0:
        print(time)
        break
    sx, sy, t = fish.pop()
    graph[sx][sy] = 0
    time += t
    s_eat += 1
    if s_eat == s_size:
        s_size += 1
        s_eat = 0
