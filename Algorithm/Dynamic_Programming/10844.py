#자릿수, 앞자리 수 메모리제이션
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n + 1)]
dp[1] = [1 for _ in range(10)]
dp[1][0] = 0

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%1000000000)
