class Solution:
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        cnt = 2
        s = list(s)
        print(s)
        while l < r:
            if s[l] != s[r]:
                s[l] = s[r]
                cnt -= 1
            l += 1
            r -= 1
        return True if cnt >= 0 else False
        