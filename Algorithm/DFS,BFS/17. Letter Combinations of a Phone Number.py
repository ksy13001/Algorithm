class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
  '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
  '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
}       
        result = []
        if not digits:
            return result

        def dfs(idx, str):
            if idx == len(digits):
                result.append(str)
                return
            for ch in mapping[digits[idx]]:
                dfs(idx+1, str+ch)

        dfs(0, "")
        return result
