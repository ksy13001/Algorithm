from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
time = 0


def safe_check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == 0 and visited[nx][ny]:
            cnt += 1
    if cnt >= 2:
        return False
    else:
        return True


def bfs(x, y):
    remove = []
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    cnt = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    que.append((nx, ny))
                elif graph[nx][ny] == 1:
                    remove.append((nx, ny))
                    cnt += 1
                visited[nx][ny] = True
    return remove


while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    remove = bfs(0, 0)
    remove1 =[]
    if len(remove) == 0:
        break
    for x, y in remove:
        if not safe_check(x, y):
            remove1.append((x, y))
    for x, y in remove1:
        graph[x][y] = 0
    time += 1
print(time)
