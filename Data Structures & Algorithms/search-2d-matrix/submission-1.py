class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, cols = len(matrix), len(matrix[0])

        l, r = 0, row * cols -1

        while l <= r:
            m = (l + r)//2 
            ROW, COL = m // cols, m % cols
            if target > matrix[ROW][COL]:
                l = m+1
            elif target < matrix[ROW][COL]:
                r = m - 1
            else: 
                return True
        return False

        