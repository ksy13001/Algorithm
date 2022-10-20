n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        now = graph[i][j]
        if 0 <= i + now < n:
            dp[i + now][j] += dp[i][j]
        if 0 <= j + now < n:
            dp[i][j + now] += dp[i][j]
