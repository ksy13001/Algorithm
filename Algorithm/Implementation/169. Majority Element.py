class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# Boyer–Moore Voting 알고리즘(과반수투표 알고리즘)
# 내가 아닌 다른 후보 투표 -> 어짜피 동률 이므로 내 count -= 1 -> hashmap 사용할 필요가 없음
# 과반수 이상이 존재 하지 않을 경우는 None return 되니 주의
