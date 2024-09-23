class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = curSum = (sum(nums[:k]))
        print(maxSum, curSum)
        for r in range(k,len(nums)):
            curSum += nums[r] - nums[r-k]
            print(maxSum, curSum)
            maxSum = max(maxSum,curSum)
        return maxSum/k
            