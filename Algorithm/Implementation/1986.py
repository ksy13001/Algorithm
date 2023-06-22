import sys
input = sys.stdin.readline
"""
4 4
2 1 4 2 4
1 1 2
1 2 3
"""
n, m = map(int, input().split())
graph = []
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
dx = [-1, -1, 1, 1, -2, 2, -2, 2]
dy = [-2, 2, -2, 2, 1, -1, -1, 1]
qx = [1, 0, -1, 0, 1, -1, 1, -1]
qy = [0, 1, 0, -1, 1, -1, -1, 1]

block = [[0 for _ in range(m)]for _ in range(n)]

# 폰
if pawn[0] != 0:
    for i in range(1, len(pawn), 2):
        block[pawn[i]-1][pawn[i+1]-1] = 1
# 나이트
if knight[0] != 0:
    for i in range(1, len(knight), 2):
        x, y = knight[i]-1, knight[i+1]-1
        block[x][y] = 1
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < m and block[nx][ny] == 0:
                block[nx][ny] = -1

# 퀸
if queen[0] != 0:
    for i in range(1, len(queen), 2):
        x, y = queen[i]-1, queen[i+1]-1
        block[x][y] = 1
        for j in range(8):
            nx = x + qx[j]
            ny = y + qy[j]
            while True:
                if 0 <= nx < n and 0 <= ny < m and (block[nx][ny] == 0 or block[nx][ny] == -1):
                    block[nx][ny] = -1
                    nx += qx[j]
                    ny += qy[j]
                else:
                    break
cnt = 0
for i in range(n):
    for j in range(m):
        if block[i][j] == 0:
            cnt += 1
print(cnt)
