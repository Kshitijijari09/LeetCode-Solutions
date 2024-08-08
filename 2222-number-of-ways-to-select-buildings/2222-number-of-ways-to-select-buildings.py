class Solution:
    def numberOfWays(self, s: str) -> int:
        
        ans = 0
        
        ones = 0
        zeroes = 0
        zero_one = 0
        one_zero = 0
        
        for char in s:
            
            
            if char == "1":
                ans += one_zero
                zero_one += zeroes
                ones += 1
                
                
            else:
                ans += zero_one
                one_zero += ones
                zeroes += 1
           
            
        return ans