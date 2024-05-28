class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        
        while l< r:
            midpoint = (l+r) // 2
            if nums[midpoint] < nums[midpoint+1]:
                l = midpoint + 1
            else:
                r = midpoint
            
        return l