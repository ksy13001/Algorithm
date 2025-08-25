class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        dp = [INF] * (amount+1)
        dp[0] = 0
        for now in range(1, amount+1):
            for coin in coins:
                if now < coin: continue
                if dp[now-coin] != INF: # 이전에 만들수 있었으면
                    dp[now] = min(dp[now], dp[now-coin]+1)
        if dp[amount] == INF:
            return -1
        return dp[amount]
