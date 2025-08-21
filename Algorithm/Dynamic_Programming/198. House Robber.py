class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [[0 for _ in range(length)]for _ in range(2)]
        dp[0][0] = nums[0]
        for i in range(1, length):
            dp[0][i] = max(dp[1][i-1] + nums[i], dp[0][i-1])
            dp[1][i] = dp[0][i-1]
        return dp[0][-1]

# 굳이 배열 안써도 되는 경우 - 열이 2개일때
class Solution1(object):
    def rob(self, nums):
        rob_not_pre, rob_pre = 0, 0
        for money in nums:
            rob_now = rob_not_pre + money
            rob_not_now = max(rob_pre, rob_not_pre)
            rob_not_pre, rob_pre = rob_not_now, rob_now
            
        return max(rob_not_pre, rob_pre)
