class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        # a = ''
        # for i in range(len(s)-1, -1, -1):
        #     a += s[i]
        # return s == a
        return s == s[::-1]
    