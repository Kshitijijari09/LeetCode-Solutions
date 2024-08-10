class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        added_coins = maxReach = 0
        coins.sort()
        
        for coin  in coins:
            while coin > maxReach + 1:
                maxReach += maxReach + 1
                added_coins += 1
                if maxReach >= target:
                    return added_coins
            maxReach += coin
            if maxReach >= target:
                return added_coins
            
        while  maxReach < target:
                maxReach += maxReach + 1
                added_coins += 1
        return added_coins