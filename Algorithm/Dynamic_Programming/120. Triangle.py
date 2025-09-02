class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for idx, val in enumerate(triangle[i]):
                dp[idx] = min(dp[idx], dp[idx+1]) + val
        return dp[0]
