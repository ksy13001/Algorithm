class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        now = 0
        for num in nums:
            now ^= num
        return now

# a^a = 0
# a^0 = a
