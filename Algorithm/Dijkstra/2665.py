import sys
import heapq
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


def dijkstra(tx, ty):
    q = []
    wall = [[INF]*n for _ in range(n)]
    heapq.heappush(q, (0, tx, ty))   # (q, (0, (0, 0)))
    wall[tx][ty] = 0
    while q:
        now_wall, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    cost = now_wall + 1
                else:
                    cost = now_wall
                if cost < wall[nx][ny]:
                    wall[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return wall[n-1][n-1]


print(dijkstra(0, 0))
