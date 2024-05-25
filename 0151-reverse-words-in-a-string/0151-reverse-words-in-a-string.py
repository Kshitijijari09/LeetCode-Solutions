class Solution:
    def reverseWords(self, s: str) -> str:
        strng = s.split()
        
        return ' '.join(strng[::-1])
        
        
            
            