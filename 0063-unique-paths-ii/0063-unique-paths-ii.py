class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [0] * n
        dp[n-1] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if grid[r][c]:
                    dp[c] = 0
                elif c+1 < n:
                    dp[c] += dp[c+1]
        return dp[0]