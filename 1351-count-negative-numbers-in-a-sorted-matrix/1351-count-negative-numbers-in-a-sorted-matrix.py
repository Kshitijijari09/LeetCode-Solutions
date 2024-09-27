class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        count = 0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    count += 1
        return count
        