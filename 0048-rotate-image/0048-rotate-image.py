class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #choose the last array 1st element
        #then choose the middle array 1st element
        #then choose the first array 1st element and repeat this for next elements.
        
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()
        
            