class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #use sliding window
        #check if the needle is the haystack
        
        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1