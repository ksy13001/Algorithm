class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        now = 0
        result = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            now_cost = g-c
            total += now_cost
            now += now_cost
            if now < 0:
                now = 0
                result = i+1
        if total < 0:
            return -1
        return result
            
# [1,2,3,4,5]
# [3,4,5,1,2]
# -2-2-2 3 3

# 4 5 1 2 3
# 1 2 3 4 5
# 3 3-2-2-2
