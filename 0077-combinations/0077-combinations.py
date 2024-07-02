class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # n = 5 [1,2,3,4] k = 2
        #output = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
                
        backtrack(1,[])
        
        return res
   
            
        
            