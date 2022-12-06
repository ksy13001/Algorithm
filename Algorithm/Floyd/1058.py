n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
friend = [[0]*n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                friend[i][j] = 1
result = 0
for i in range(n):
    result = max(result, friend[i].count(1))
print(result)
