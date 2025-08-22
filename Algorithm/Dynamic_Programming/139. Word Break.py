class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        max_length = max(map(lambda x:len(x), wordDict))
        min_length = min(map(lambda x:len(x), wordDict))
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for length in range(min_length, max_length+1):
                j = i - length
                if j<0:
                    continue
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
