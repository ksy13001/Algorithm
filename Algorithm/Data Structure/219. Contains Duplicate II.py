# 50
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, x in enumerate(nums):
            if x in dic:
                if i - dic[x] <= k:
                    return True
            dic[x] = i
        return False 
            

        # 시간초과 
        # s = set()
        # for i in range(len(nums)):
        #     print(s)
        #     if nums[i] in s:
        #         return True
        #     s.add(nums[i])
        #     if i >= k:
        #         s.remove(nums[i-k])
        # return False
    
