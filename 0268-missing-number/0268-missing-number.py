class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(len(nums)):
            print(i,nums[i])
            n += (i - nums[i])
            print(n)
        return n
            
