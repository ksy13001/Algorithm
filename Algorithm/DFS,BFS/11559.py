import sys, time
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


graph = []
for _ in range(12):
    graph.append(list(input().rstrip()))


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    route = [(sx, sy)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == graph[sx][sy] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                route.append((nx, ny))
    if len(route) >= 4:
        return route
    else:
        return -1


def bomb(target):
    for arr in target:
        for x, y in arr:
            graph[x][y] = '.'


def fall():
    block = False
    now = -1
    q = deque([])
    for y in range(6):
        for x in range(11, -1, -1):
            if graph[x][y] != '.':
                while x < 11 and graph[x+1][y] == '.':
                    graph[x][y], graph[x+1][y] = graph[x+1][y], graph[x][y]
                    x += 1


ans = 0
while True:
    target = []
    visited = [[False for _ in range(6)] for _ in range(12)]
    check = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                temp = bfs(i, j)
                if temp != -1:
                    check = True
                    target.append(temp)
    # 터뜨리기
    bomb(target)
    # 낙하
    fall()
    """
    for i in range(12):
        print(graph[i])
    print()
    """
    if not check:
        print(ans)
        break
    else:
        ans += 1
