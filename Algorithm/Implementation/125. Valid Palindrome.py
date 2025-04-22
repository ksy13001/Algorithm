class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s)-1
        while start < end:
            if s[start].lower() != s[end].lower():
                if not s[start].isalnum():
                    start+= 1
                elif not s[end].isalnum():
                    end -= 1
                else:
                    return False
            else:
                start += 1
                end -= 1
        return True
