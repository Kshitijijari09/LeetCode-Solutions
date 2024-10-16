class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = len(nums)+1
        CurSum = 0
        
        for r , n in enumerate(nums):
            CurSum += n
            while CurSum >= target:
                res = min(res,r-l+1)
                print(res)
                CurSum -= nums[l]
                l+=1
        return res if res <= len(nums) else 0
    
    
    
    