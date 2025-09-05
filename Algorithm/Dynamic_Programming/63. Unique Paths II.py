class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        n, m = len(og), len(og[0])
        dp = [0 for _ in range(m)]
        for i in range(m):
            if og[0][i] == 1:
                break
            dp[i] = 1
        
        for i in range(1, n):
            for j in range(m):
                if og[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] += dp[j-1]
        return dp[m-1]
