class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        stack = [0 for _ in range(101)]
        for n in nums:
            stack[n] += 1
        pre = [0 for _ in range(101)]
        now = 0
        for i in range(len(stack)):
            pre[i] += now
            now += stack[i]

        return [pre[x] for x in nums]
