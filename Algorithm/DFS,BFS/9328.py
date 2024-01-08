import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x0, y0, lock):
    q = deque([(x0, y0)])
    visited[x0][y0] = True
    ans = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            def go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] != '*':
                if graph[nx][ny] == '.':
                    go(nx, ny)
                elif graph[nx][ny] == '$':
                    ans += 1
                    go(nx, ny)
                # 소문자 키일 경우
                elif graph[nx][ny].islower():
                    go(nx, ny)
                    # 처음 줍는 키일 경우
                    if graph[nx][ny].upper() not in key:
                        key[graph[nx][ny].upper()] = graph[nx][ny]
                        # 이전에 만났던 잠긴 문 열기
                        for now in lock:
                            if now[0].lower() == graph[nx][ny]:
                                q.append((now[1], now[2]))
                                visited[now[1]][now[2]] = True
                # 키 가 있을 경우
                elif graph[nx][ny].isupper():
                    if graph[nx][ny] in key:
                        go(nx, ny)
                    # 키 없는 경우
                    else:
                        lock.append((graph[nx][ny], nx, ny))
    #print('lock:', lock)
    #print('key:', key)
    return ans


for _ in range(int(input().rstrip())):
    h, w = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    arr = list(input().rstrip())
    key = {}
    lock = []
    for k in arr:
        if k != '0':
            key[k.upper()] = k
    visited = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    # 가장자리 탐색
    for i in range(h):
        for j in range(w):
            if (i == 0 or i == h-1 or j == 0 or j == w-1) and graph[i][j] != '*' and not visited[i][j]:
                if graph[i][j] == '.':
                    ans += bfs(i, j, lock)
                elif graph[i][j].islower():
                    key[graph[i][j].upper()] = graph[i][j]
                    ans += bfs(i, j, lock)
                elif graph[i][j].isupper():
                    if graph[i][j] in key:
                        ans += bfs(i, j, lock)
                    else:
                        lock.append((graph[i][j], i, j))
                elif graph[i][j] == '$':
                    ans += bfs(i, j, lock)
                    ans += 1
    print(ans)
