def solution(park, routes):
    n, m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                sx, sy = i, j

    for route in routes:
        d, moves = route.split(" ")
        sx, sy = move(sx, sy, park, n, m, d, int(moves))
        print(sx, sy)
    return [sx, sy]


def move(nx, ny, park, n, m, d, moves):
    sx, sy = nx, ny
    x, y = 0, 0
    if d == "N":
        x = -1
    elif d == "E":
        y = 1
    elif d == "W":
        y = -1
    elif d == "S":
        x = 1
    for i in range(moves):
        nx += x
        ny += y
        if  nx < 0 or nx > n-1 or ny < 0 or ny > m-1 or park[nx][ny] == 'X':
            return (sx, sy)
    return (nx, ny)
