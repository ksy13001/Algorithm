class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, temp, n = 0, 0, 0, len(nums)
        ans = n + 1
        while end <= n:
            if temp >= target:
                ans = min(ans, end - start)
                temp -= nums[start]
                start += 1
            else:
                if end == n:
                    break
                temp += nums[end]
                end += 1
        if ans == n+1:
            return 0
        return ans
