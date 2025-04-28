class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height) - 1
        result = 0
        while start < end:
            result = max(result, min(height[start], height[end])*(end-start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return result
