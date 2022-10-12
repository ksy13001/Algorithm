#12865.py 표 그려서 해결하기
n, k = map(int, input().split())
item = [[0, 0]]
for _ in range(n):
    item.append(list(map(int, input().split())))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, k + 1):
        if item[i][0] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i-1][j], item[i][1] + dp[i - 1][j - item[i][0]])
print(dp[n][k])
