class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n-2, -1, -1):
            for idx, value in enumerate(triangle[i]):
                dp[idx] = min(dp[idx], dp[idx+1]) + value
        return dp[0]
