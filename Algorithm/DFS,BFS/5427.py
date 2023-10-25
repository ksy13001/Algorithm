import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(sx, sy):
    sq = deque([(sx, sy)])
    fq = deque(fire)
    s_visited = [[0 for _ in range(m)] for _ in range(n)]
    s_visited[sx][sy] = 1
    now = 2
    cnt = 0
    while sq:
        x, y = sq.popleft()
        if graph[x][y] == '.' or graph[x][y] == '@':
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                return s_visited[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and s_visited[nx][ny] == 0:
                    if graph[nx][ny] == '.':
                        sq.append((nx, ny))
                        s_visited[nx][ny] = s_visited[x][y] + 1
                        cnt = max(cnt, s_visited[nx][ny])
            if cnt == now:
                now += 1
                k = len(fq)
                for _ in range(k):
                    x, y = fq.popleft()
                    for i in range(4):
                        fx = x + dx[i]
                        fy = y + dy[i]
                        if 0 <= fx < n and 0 <= fy < m and graph[fx][fy] == '.':
                            graph[fx][fy] = '*'
                            fq.append((fx, fy))
    return -1


for _ in range(int(input())):
    m, n = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(input().rstrip()))
    fire = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                fire.append((i, j))
            if graph[i][j] == '@':
                sx, sy = i, j
    ans = bfs(sx, sy)
    if ans == -1:
        ans = 'IMPOSSIBLE'
    print(ans)


