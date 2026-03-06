class SolutionV1:
    def lengthOfLongestSubstringV1(self, s: str) -> int:
        dic = {}
        left = 0
        ans = 0
        for right, st in enumerate(s):
            if st in dic:
                left = max(left, dic[st] + 1)
            dic[st] = right
            ans = max(ans, right - left + 1)
        return ans

     def lengthOfLongestSubstringV2(self, s: str) -> int:
        ans = 0
        left = 0
        now = set()
        for right in range(len(s)):
            while s[right] in now:
                now.remove(s[left])
                left += 1

            now.add(s[right])
            ans = max(ans, len(now))

        return ans

"""
abcbdg
{a, b, c}
"""
