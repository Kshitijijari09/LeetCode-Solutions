class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        a = ''
        for i in range(len(s)-1, -1, -1):
            a += s[i]
            print(a)
        return s == a
    