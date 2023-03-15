import math

def com(n, k):
    dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]


n, m = map(int, input().split())
print(com(n, m))
#print(math.comb(n, m)) 
