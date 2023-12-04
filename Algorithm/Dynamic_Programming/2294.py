INF = int(1e9)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [INF for _ in range(k+1)]
dp[0] = 0
# 가능한 코인 탐색
for coin in coins:
    # 현재 사용 코인보다 더 큰 수 중 값 갱신 
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
