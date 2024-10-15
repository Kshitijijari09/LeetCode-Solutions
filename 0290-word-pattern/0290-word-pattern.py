class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        di = {}
        li = s.split(" ")
        if len(pattern) != len(li):
            return False
        for i, val in enumerate(pattern):
            if val in di and di[val] != li[i]:
                return False
            elif val not in di and li[i] in di.values():
                return False
            elif val not in di:
                di[val] = li[i]
        return True