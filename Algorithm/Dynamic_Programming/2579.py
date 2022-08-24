n = int(input())
stair = [0] *(n+2)
dp = [0] * (n+2)
for i in range(n):
    stair[i] = int(input())
dp[0] = stair[0]
dp[1] = stair[1]+stair[0]
dp[2] = stair[2] + max(stair[0], stair[1])
for i in range(3, n):
    dp[i] = stair[i] + max(dp[i-2], dp[i-3] + stair[i-1])
print(dp[n-1])
