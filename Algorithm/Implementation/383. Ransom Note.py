class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        #97
        arr = [0] * 26
        for m in magazine:
            arr[ord(m)-97] += 1
        
        for r in ransomNote:
            idx = ord(r)-97
            if arr[idx] <= 0:
                return False
            arr[idx] -= 1
        return True
        
