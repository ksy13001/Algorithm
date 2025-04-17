class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        length = min(map(len, strs))
        for i in range(length):
            now = strs[0][i]
            for j in range(1, len(strs)):
                if now != strs[j][i]:
                    return result
            result += now
        return result
