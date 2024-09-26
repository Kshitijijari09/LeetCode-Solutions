class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_ones = 0
        l = 0
        zeroes = 0
        
        if len(nums) == sum(nums):
            return sum(nums)-1
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            print(zeroes)
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l +=1
            max_ones = max(max_ones,r-l)
            print(l,r,max_ones)
        return max_ones