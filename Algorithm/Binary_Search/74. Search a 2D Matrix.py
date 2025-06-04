
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix += [[10**4+1]]
        for i in range(1, len(matrix)):
            if matrix[i-1][0] <= target < matrix[i][0]:
                if target in matrix[i-1]:
                    return True
                return False
        return False
