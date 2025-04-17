class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if result != 0:
                    return result
            else:
                result += 1
        return result
