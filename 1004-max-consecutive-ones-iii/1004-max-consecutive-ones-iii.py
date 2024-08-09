class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        l = 0
        zeroes = 0
        n = len(nums)
        
        for r in range(n):
            if nums[r] == 0:
                zeroes += 1
                
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            w = r - l + 1
            max_ones = max(max_ones, w)
        return max_ones