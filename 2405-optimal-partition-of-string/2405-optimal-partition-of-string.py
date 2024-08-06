class Solution:
    def partitionString(self, s: str) -> int:
        
        charset = set()
        res = 1
        
        for c in s:
            if c in charset:
                res += 1
                charset = set()
            charset.add(c)
        return res