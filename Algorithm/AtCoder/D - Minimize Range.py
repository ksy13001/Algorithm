from collections import deque

def sol():
    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(input()))

    def bfs(x, y, visited):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        q = deque()
        if visited[x][y]:
            return 0
        q.append((x, y))
        out = False

        while q:
            x, y = q.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if nx == 0 or nx == n - 1 or ny ==0 or ny == m - 1:
                        out = True

        if out:
            return 0
        else:
            return 1



    visited = [[False] * m for _ in range(n)]

    ans = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] == ".":
                ans += bfs(i, j, visited)
    print(ans)



sol()

"""
4
start 1: 25 40 65
start 2: 30 55
start 3: 25
 to 2 = 25
 to 3 = 40 or 25 + 30
 to 4 = 
"""
