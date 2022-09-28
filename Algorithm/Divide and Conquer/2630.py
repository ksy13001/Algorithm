import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
blue = 0
white = 0


def divide(n, g):
    global blue, white
    temp = 0
    for i in range(n):
        temp += sum(g[i])
    if temp == 0:
        white += 1
    elif temp == n*n:
        blue += 1
    else:
        divide(n//2, [row[0:n//2] for row in g[0:n//2]])
        divide(n//2, [row[0:n//2] for row in g[n//2:n]])
        divide(n//2, [row[n//2:n] for row in g[0:n//2]])
        divide(n//2, [row[n//2:n] for row in g[n//2:n]])


divide(n, graph)
print(white)
print(blue)
