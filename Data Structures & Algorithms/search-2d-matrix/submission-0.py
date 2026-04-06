class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force
        for p1 in range(len(matrix)):
            for num in matrix[p1]:
                if num == target:
                    return True

        return False