from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
q_fire = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            sx, sy = i, j
        if graph[i][j] == 'F':
            q_fire.append((i, j))


def bfs():
    q = deque([(sx, sy)])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited_fire = [[False for _ in range(m)] for _ in range(n)]
    visited[sx][sy] = 1
    now = 1
    cnt = 2
    while q:
        # 지훈 이동
        x, y = q.popleft()
        if graph[x][y] != 'F':
            if x == 0 or x == n-1 or y == 0 or y == m-1:
                return visited[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    if graph[nx][ny] == '.':
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        now = max(visited[nx][ny], now)

        # 불 번지기
        if cnt == now:
            k = len(q_fire)
            for _ in range(k):
                fx, fy = q_fire.popleft()
                visited_fire[fx][fy] = True
                for i in range(4):
                    nfx = fx + dx[i]
                    nfy = fy + dy[i]
                    if 0 <= nfx < n and 0 <= nfy < m and not visited_fire[nfx][nfy]:
                        if graph[nfx][nfy] == '.':
                            graph[nfx][nfy] = 'F'
                            q_fire.append((nfx, nfy))
                            visited_fire[nfx][nfy] = True
            cnt += 1

    return 'IMPOSSIBLE'


print(bfs())


