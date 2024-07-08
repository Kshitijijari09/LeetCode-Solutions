class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i=0
            for j in nums:
                if j<target:
                    i+=1
                else:
                    break
            return i