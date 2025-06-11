class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n != 1:
            n = self.digit_sum(n)
            if n in visited:
                return False
            visited.append(n)
        return True

    def digit_sum(self, num:int)->int:
        result = 0
        while num >= 10:
            result += (num%10)**2
            num //= 10
        return result + num**2
