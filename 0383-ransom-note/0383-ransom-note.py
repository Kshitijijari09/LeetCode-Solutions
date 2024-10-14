class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mg = Counter(magazine)
        
        for key in rn:
            if key not in mg:
                return False
            else:
                if rn[key] > mg[key]:
                    return False
        return True