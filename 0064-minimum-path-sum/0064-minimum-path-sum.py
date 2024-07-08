class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid),len(grid[0])
        
#         res = [[float("inf")] * (cols + 1) for i in range(rows + 1)]
#         res[rows - 1][cols] = 0
        
#         for r in range(rows-1,-1,-1):
#             for c in range(cols-1,-1,-1):
#                 res[r][c] = grid[r][c] + min(res[r+1][c],res[r][c+1])
#                 print(res[r][c])
#         return res[0][0]
          
    
        n = len(grid)
        m = len(grid[0])

        # Edit the first row:
        for i in range(1, m):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        

        # Edit the first col:
        for i in range(1, n):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        
            
        # Edit the remaining values in the grid accordingly!
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        return grid[-1][-1]