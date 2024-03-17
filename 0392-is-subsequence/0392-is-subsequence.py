class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j =0,0
        if len(s) == 0:
            return True
        if len(s) == 0 and len(t) == 0:
            return True
        
        while j < len(t):
            if s[i] == t[j]:
                print(s[i],t[j], i, j)
                i+=1
                j+=1
                print(i,j)
            else:
                j+=1
                
            if i == len(s):
                return True
            print(i,j)
        return False