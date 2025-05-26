class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        arr = [0 for i in range(26)]
        for i in range(ls):
            arr[ord(s[i])-97] += 1
            arr[ord(t[i])-97] -= 1
        for alpha in arr:
            if alpha != 0:
                return False
        return True
