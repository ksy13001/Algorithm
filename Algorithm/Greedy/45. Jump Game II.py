INF = int(1e9)
class Solution(object):
    def jump(self, nums):
        # 현재 가장 멀리 갈수 있는곳을 저장
        n = len(nums)
        high = 0
        now = nums[0]
        result = 0
        if n <= 1:
            return 0
        for i in range(n-1):
            high = max(high, nums[i] + i)
            if i == now:
                result += 1
                now = high
        return result + 1
