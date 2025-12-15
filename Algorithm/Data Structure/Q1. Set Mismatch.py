class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        idx = [0 for _ in range(len(nums)+1)]
        for n in nums:
            idx[n] += 1
        result = [-1, -1]
        for i in range(1, len(idx)):
            if idx[i] == 2:
                result[0] = i
            elif idx[i] == 0:
                result[1] = i
        return result
