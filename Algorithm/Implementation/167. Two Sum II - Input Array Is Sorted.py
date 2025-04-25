class Solution(object):
    def twoSum(self, numbers, target):
        # 현재 합보다 target 이크면    start += 1
        # 현재 합보다 target 이 작으면 end -= 1
        start, end = 0, len(numbers)-1
        while start < end:
            now = numbers[start] + numbers[end]
            if now == target:
                return [start+1, end+1]
            elif now < target:
                start += 1
            else:
                end -= 1
        return
