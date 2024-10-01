class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_last_element(isfirst):
            l, r = 0,len(nums) -1
            idx = -1

            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    idx = mid
                    if isfirst:
                        r = mid - 1
                    else:
                        l = mid + 1
                        
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx
    
        first = first_last_element(True)
        last = first_last_element(False)
        return [first,last]