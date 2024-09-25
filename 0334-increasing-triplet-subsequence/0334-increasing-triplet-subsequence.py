class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
                print("f",first)
            elif num <= second:  
                second = num
                print(second)
            else:  # Now first < second < num
                return True
        return False