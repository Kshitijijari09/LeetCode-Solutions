class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            print(i,letter_group)
            print(set(letter_group))
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
            