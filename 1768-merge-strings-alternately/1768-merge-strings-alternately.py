class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        iterate = min(len(word1),len(word2))
        for i in range(iterate):
            res += word1[i] + word2[i]
            
        return res + word1[i+1:] + word2[i+1:]
            