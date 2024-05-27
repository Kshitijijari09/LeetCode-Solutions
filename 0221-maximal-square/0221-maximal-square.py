class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        
        def squares(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r,c) not in cache:
                down = squares(r+1,c)
                right = squares(r,c+1)
                diag = squares(r+1,c+1)
                
                cache[(r,c)] = 0
                
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down,right,diag)
                
            return cache[(r,c)]
        squares(0,0)
        
        return max(cache.values()) ** 2