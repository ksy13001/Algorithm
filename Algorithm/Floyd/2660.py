INF = int(1e9)
n = int(input())
graph = [[INF]*(n+1)for _ in range(n+1)]
friend = [[0]*(n+1)for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n+1):
    graph[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
score = INF
can = []
for i in range(1, n+1):
    score = min(max(graph[i][1:]), score)
for j in range(1, n+1):
    if max(graph[j][1:]) == score:
        can.append(j)
print(score, len(can))
print(*can)
