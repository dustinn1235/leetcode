# do binary search
# matrix m * n
# i = index // n
# j = index mod n 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])
            if target == matrix[i][j]:
                return True
            
            if target < matrix[i][j]:
                r = mid - 1
            else:
                l = mid + 1
        return False
            