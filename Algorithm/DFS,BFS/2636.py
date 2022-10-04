from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
count = []
time = 0


def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
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
                    graph[nx][ny] = 0
                    cnt += 1
                visited[nx][ny] = True
    count.append(cnt)
    return cnt


while True:
    c = bfs(0, 0)
    if c == 0:
        break
    time += 1
print(time)
print(count[-2])
