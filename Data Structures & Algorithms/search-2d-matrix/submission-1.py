# O(log(m*n)) - time. O(1) - space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        matrixSize = m * n
        left, right = 0, matrixSize - 1

        while left <= right:
            mid = (left + right + 1) // 2
            row, column = mid // n, mid % n
            number = matrix[row][column]

            if number > target:
                right = mid - 1
            elif number < target:
                left = mid + 1
            else:
                return True

        
        return False