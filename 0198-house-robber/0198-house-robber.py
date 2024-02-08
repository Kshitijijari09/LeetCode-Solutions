class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1,sum2 = 0,0
        
        for i in nums:
            tmp = max(i + sum1,sum2)
            sum1 = sum2
            sum2 = tmp
        return sum2
        
       