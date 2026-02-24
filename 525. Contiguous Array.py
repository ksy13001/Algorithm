class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        prefix = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix not in dic:
                dic[prefix] = i
            else:
                ans = max(ans, i - dic[prefix])
        return ans





"""
        0   1  2  3  4  5  6  7  8  9  10
nums = [0,  1, 1, 1, 1, 1, 0, 0, 0, 1, 0]
cnts = [-1, 0, 1, 2, 3, 4, 3, 2, 1, 2, 1]
"""
