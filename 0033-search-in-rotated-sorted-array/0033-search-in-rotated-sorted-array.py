class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l<=r:
            if target not in nums:
                return -1
            
            if target == nums[l]:
                return l
            else:
                l += 1
         # return nums.index(target) if target in nums else -1