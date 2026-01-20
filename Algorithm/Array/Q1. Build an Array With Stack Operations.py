class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        idx = 0
        for num in range(1, target[-1]+1):
            ans.append("Push")
            if target[idx] != num:
                ans.append("Pop")
                continue
            idx +=1 
            
        return ans
