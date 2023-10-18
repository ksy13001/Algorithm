import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
jx = [2, 1, -2, 1, -1, 2, -1, -2]
jy = [1, 2, 1, -2, 2, -1, -2, -1]
k = int(input())
m, n = map(int, input().split())


graph = []
visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs():
    q = deque([(0, 0, 0, 0)])
    while q:
        #print(q)
        x, y, cnt, jump = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][jump] and graph[nx][ny] == 0:
                q.append((nx, ny, cnt + 1, jump))
                visited[nx][ny][jump] = True
        if jump < k:
            for i in range(8):
                nx = x + jx[i]
                ny = y + jy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][jump+1] and graph[nx][ny] == 0:
                    q.append((nx, ny, cnt + 1, jump + 1))
                    visited[nx][ny][jump+1] = True
    return -1


print(bfs())
