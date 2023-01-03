import sys
input = sys.stdin.readline
dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]
graph = []
n = 19
for _ in range(n):
    graph.append(list(map(int, input().split())))


def sol(x, y, color):
    for i in range(4):
        cnt = 1
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 > nx or nx >= n or ny < 0 or ny >= n:
                break
            if graph[nx][ny] != color:
                break
            else:
                cnt += 1
        if cnt == 5:
            if graph[x-dx[i]][y-dy[i]] != color or x == 0:
                if color == 1:
                    return 1
                else:
                    return 2
    return 0


ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            a = sol(i, j, graph[i][j])
            if a > 0:
                ans = (a, i+1, j+1)
if ans == 0:
    print(0)
else:
    print(ans[0])
    print(ans[1], ans[2])
