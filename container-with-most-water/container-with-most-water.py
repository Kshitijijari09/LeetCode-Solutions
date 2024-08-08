class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Lets have two pointers pointing the heights L and R
        A = 0
        l,r = 0,len(height)-1

        while l<r:
            maxA = (r-l) * min(height[l],height[r])
            A = max(A, maxA)
            if height[l] == height[r] or height[r]>height[l]:
                l += 1
            elif height[l]>height[r]:
                r -= 1
        return A