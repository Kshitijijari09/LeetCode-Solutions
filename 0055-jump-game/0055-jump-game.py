class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= reach:
                reach = i
            
        return True if reach == 0 else False