class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = self.digit_sum(n)
        return n==1

    def digit_sum(self, num:int)->int:
        result = 0
        while num > 0:
            result += (num%10)**2
            num //= 10
        return result
