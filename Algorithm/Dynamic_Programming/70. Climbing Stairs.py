class Solution:
    def climbStairs(self, n: int) -> int:
        dp_1 = 1
        dp_2 = 2
        if(n<=2):
            return n
        for i in range(3, n+1):
            dp_n = dp_1 + dp_2
            dp_1 = dp_2
            dp_2 = dp_n
        return dp_n
