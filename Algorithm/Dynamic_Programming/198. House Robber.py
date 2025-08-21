class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [[0 for _ in range(length)]for _ in range(2)]
        dp[0][0] = nums[0]
        for i in range(1, length):
            dp[0][i] = max(dp[1][i-1] + nums[i], dp[0][i-1])
            dp[1][i] = dp[0][i-1]
        return dp[0][-1]
