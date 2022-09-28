n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def comp(n, g):
    temp = 0
    for i in range(n):
        temp += sum(g[i])
    if temp == 0:
        print(0, end='')
    elif temp == n*n:
        print(1, end='')
    elif n == 2:
        print('(', end='')
        for i in range(n):
            for j in range(n):
                print(g[i][j], end='')
        print(')', end='')
    else:
        print('(', end='')
        comp(n//2, [row[0:n//2] for row in g[0:n//2]])
        comp(n//2, [row[n//2:n] for row in g[0:n//2]])
        comp(n//2, [row[0:n//2] for row in g[n//2:n]])
        comp(n//2, [row[n//2:n] for row in g[n//2:n]])
        print(')', end='')


comp(n, graph)
