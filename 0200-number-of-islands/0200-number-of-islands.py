class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
        
#         rows,cols = len(grid),len(grid[0])
#         visit = set()
#         islands = 0

#         def bfs(r,c):
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
#             while q:
#                 row,col = q.popleft()
#                 directions = [[1,0],[-1,0],[0,1],[0,-1]]
#                 for dr,dc in directions:
#                     r,c = row + dr,col + dc
#                     if (r in range(rows) and 
#                         c in range(cols) and 
#                         (r,c) not in visit and 
#                         grid[r][c] == "1" ):
#                         q.append((r,c))
#                         visit.add((r,c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r,c) not in visit:
#                     bfs(r,c)
#                     islands += 1
#         return islands


        if not grid:
            return 0
        
        Rows, Cols = len(grid),len(grid[0])
        island = 0 
        visit = set()
        
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    ROWS, COLS = dr+row,dc+col
                    if (ROWS in range(Rows) and 
                        COLS in range(Cols) and 
                        (ROWS,COLS) not in visit and 
                        grid[ROWS][COLS] == "1"):
                        q.append((ROWS,COLS))
                        visit.add((ROWS,COLS))
      
        
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        return island 