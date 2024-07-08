class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lst = []
        # for first and last cols
        for r in range(rows):
            if target >= matrix[r][0] and target <= matrix[r][cols-1]:
                for c in range(cols):
                    lst.append(matrix[r][c])
        
        return True if target in lst else False
        