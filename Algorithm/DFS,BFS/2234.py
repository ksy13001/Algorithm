from collections import deque
import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
""" 
8421    남동북서    1 -> wall / 0 -> open
7 4
11      6       11      6       3       10      6
7       9       6       13      5       15      5
1       10      12      7       13      7       5
13      11      10      8       10      12      13
----------------------------------------------------
1011    0110    1011    0110    0011    1010    0110
0111    1001    0110    1101    0101    1111    0101
0001    1010    1100    0111    1101    0111    0101
1101    1011    1010    1000    1010    1100    1101
----------------------------------------------------
"""


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[x][y] & (1<<i) == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    return cnt


group = []
broken = []
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            group.append(bfs(i, j))


visited = [[False for _ in range(m)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            for k in range(4):
                if graph[i][j] & (1<<k) != 0:
                    graph[i][j] -= (1<<k)
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    visited[i][j] = True
                    ans = max(bfs(i, j), ans)
                    graph[i][j] += (1<<k)

print(len(group))
print(max(group))
print(ans)
