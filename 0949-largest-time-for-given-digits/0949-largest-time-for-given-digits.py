class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        maxtime = -1
        
        for perm in permutations(arr):
            h1,h2,m1,m2 = perm
            hr = h1*10+h2
            m = m1*10 + m2
            if hr < 24 and m < 60:
                maxtime = max(maxtime, hr*60+m)
        if maxtime == -1:
            return ""
        else:
            return f"{maxtime // 60:02}:{maxtime % 60:02}"
            