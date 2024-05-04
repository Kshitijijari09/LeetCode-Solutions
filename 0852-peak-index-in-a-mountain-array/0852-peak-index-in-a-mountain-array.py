class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0, len(arr)-1
        
        while l< r:
            midpoint = (l+r) // 2
            print(midpoint)
            if arr[midpoint] < arr[midpoint+1]:
                l = midpoint + 1
            else:
                r = midpoint
            
        return l
            # return arr.index(max(arr))