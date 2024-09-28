class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions for binary search
        potions.sort()
        res = []
        
        # For each spell, find how many potions can form a successful pair
        for spell in spells:
            # Calculate the threshold for a successful pair
            threshold = (success + spell - 1) // spell  # ceil(success / spell)
            # thres1 = math.ceil(success / spell)
            

            # Perform manual binary search to find the first potion >= threshold
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < threshold:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # All potions from `left` to the end are successful pairs
            count = len(potions) - left
            res.append(count)
        
        return res
    