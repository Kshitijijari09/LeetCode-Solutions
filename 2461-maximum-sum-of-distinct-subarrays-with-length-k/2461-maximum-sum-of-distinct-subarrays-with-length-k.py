class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l,r = 0 , 0
        mx, tot = 0,0
        visit = set()
        
        while r < len(nums):
            while nums[r] in visit:
                tot -= nums[l]
                visit.remove(nums[l])
                l += 1
            tot += nums[r]
            visit.add(nums[r])
            if r-l+1 == k:
                mx = max(mx,tot)
                tot -= nums[l]
                visit.remove(nums[l])
                l += 1
            r += 1
        return mx