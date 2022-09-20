import sys
from collections import deque
#pypy
#무한반복, 반복문 돌면서 전체 확인, bfs로는 개방 가능한 구역 찾고 값 갱신하기

input = sys.stdin.readline
n, l, r = map(int, input().split())
gap = r - l
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
check = False


def bfs(x, y):
    global check, visited
    cnt = 1
    union = [(x,y)]
    temp = graph[x][y]
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        visited[x][y] = True
        now = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - now) <= r:
                    union.append((nx, ny))
                    temp += graph[nx][ny]
                    cnt += 1
                    visited[nx][ny] = True
                    que.append((nx, ny))
    temp //= cnt
    if cnt > 1:
        if union:
            for tx, ty in union:
                graph[tx][ty] = temp
                check = True


while True:
    check = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
    if not check:
        break
    else:
        result += 1
print(result)
