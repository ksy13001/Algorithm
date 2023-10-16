import sys
input = sys.stdin.readline

n = int(input())
st = input().rstrip()
arr = [['.']*n for _ in range(n)]
d = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
x, y = 0, 0


def move(s):
    if s == 'D':
        if arr[x][y] == '.' or arr[x][y] == '|':
            arr[x][y] = '|'
        else:
            arr[x][y] = '+'
    if s == 'U':
        if arr[x][y] == '.' or arr[x][y] == '|':
            arr[x][y] = '|'
        else:
            arr[x][y] = '+'
    if s == 'L':
        if arr[x][y] == '.' or arr[x][y] == '-':
            arr[x][y] = '-'
        else:
            arr[x][y] = '+'
    if s == 'R':
        if arr[x][y] == '.' or arr[x][y] == '-':
            arr[x][y] = '-'
        else:
            arr[x][y] = '+'


for s in st:
    if s == 'D':
        if x < n - 1:
            move('D')
            x += 1
            move('D')
    if s == 'U':
        if x > 0:
            move('U')
            x -= 1
            move('U')
    if s == 'L':
        if y > 0:
            move('L')
            y -= 1
            move('L')
    if s == 'R':
        if y < n-1:
            move('R')
            y += 1
            move('R')
for i in range(n):
    print(''.join(arr[i]))
