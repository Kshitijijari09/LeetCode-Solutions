class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        cache = {}
        
        for idx in range(len(nums)):
            if (target - nums[idx]) in cache:
                return [cache[target-nums[idx]], idx]
            cache[nums[idx]] = idx
        return -1 
        