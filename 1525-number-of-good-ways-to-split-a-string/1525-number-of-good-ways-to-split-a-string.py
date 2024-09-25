class Solution:
    def numSplits(self, s: str) -> int:
        left_counter = Counter()
        right_counter = Counter(s)
        count = 0
        left_unique = 0
        right_unique = len(right_counter)
        
        for i in range(len(s)):
            left_counter[s[i]] += 1
            if left_counter[s[i]] == 1:
                left_unique += 1
            
            right_counter[s[i]] -= 1
            if right_counter[s[i]] == 0:
                right_unique -= 1
            
            if left_unique == right_unique:
                count += 1
        return count