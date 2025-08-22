class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) < min(map(len, wordDict)):
            return False
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                j = i-len(w)
                if j<0:continue
                if dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
                    break
        return dp[n]
