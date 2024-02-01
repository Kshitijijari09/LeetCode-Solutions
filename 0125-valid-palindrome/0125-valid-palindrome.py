class Solution:
    def isPalindrome(self, s: str) -> bool:
        st= ""
        for i in s:
            if i.isalnum():
                st += i
        print(st)
        
        length = len(st)
        
        l,r = 0,len(st)-1
        
        if length == 0:
            return True

        while l < r:  
            if st[l].lower() == st[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
                
            
            
        
        
            