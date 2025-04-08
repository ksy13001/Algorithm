class Solution(object):
    def canJump(self, nums):
        now = len(nums)-1
        for i in range(now-1, -1, -1):
            if nums[i] + i >= now:
                now = i
        return now == 0

# 역으로 생각하기 - 시작점에서 출발해서 도착점으로 가는 경우의 수는 많지만 
# 도착점에서 출발점으로 갈때는 도달 가능한지만 확인하면됨
