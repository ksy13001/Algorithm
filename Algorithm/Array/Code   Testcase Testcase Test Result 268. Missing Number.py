class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n=3 [3,0,1] -> 1, 2, 3 존재해야함
        # 인덱스 xor num 하면 값 날라감

        ans = 0
        for i, num in enumerate(nums):
            ans ^= (i+1)^num
        return ans
