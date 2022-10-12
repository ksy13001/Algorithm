n, k = map(int, input().split())
INF = int(1e9)
memory = [0] + list(map(int, input().split()))
value = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(value) + 1)] for _ in range(n + 1)]
result = sum(value)
for i in range(1, n + 1):
    for j in range(1, sum(value) + 1):
        if value[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], memory[i] + dp[i-1][j-value[i]])
            if dp[i][j] >= k:
                result = min(result, j)

print(result)
