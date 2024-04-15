class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ht = len(mat)
        w = len(mat[0])
        
        q = []
        
        for i in range(ht):
            for j in range(w):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j]="#"
                    
        for row, col in q:
            for dr, dy in (1,0),(-1,0),(0,1),(0,-1):
                nr = row + dr
                nc = col + dy
                
                if 0<=nr<ht and 0<=nc<w and mat[nr][nc]=='#':
                    mat[nr][nc] = mat[row][col]+1
                    q.append((nr,nc))
        return mat 