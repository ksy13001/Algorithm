from collections import deque
n = int(input())
k = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
l = int(input())
move = []
for _ in range(l):
    c, d = map(str, input().split())
    move.append((int(c), d))
dn = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
tm = 0
snake = deque()
now = [0, 0]
snake.append((now[0], now[1]))
while True:
    if tm < l:
        if time == move[tm][0]:
            if move[tm][1] == 'D':
                dn += 1
            else:
                dn -= 1
            dn %= 4
            tm += 1
    graph[now[0]][now[1]] = 2
    now[0] += dx[dn]
    now[1] += dy[dn]
    time += 1
    if now[0] < 0 or now[0] >= n or now[1] < 0 or now[1] >= n or graph[now[0]][now[1]] == 2:
        print(time)
        print(snake)
        break
    snake.append((now[0], now[1]))
    print(now, end=' ')
    if graph[now[0]][now[1]] == 0:
        x, y = snake.popleft()
        graph[x][y] = 0
    graph[now[0]][now[1]] = 2
    print(snake)
