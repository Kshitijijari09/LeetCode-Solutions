class Solution:
    def countOrders(self, n: int) -> int:
        
        
        slots = 2*n #total number of choices but not valid 
        res = 1
        while slots>0:
            valid_choices = slots * (slots -1 )//2 # total valid choices
            res *= valid_choices
            slots -=2
        return res % (10**9+7)