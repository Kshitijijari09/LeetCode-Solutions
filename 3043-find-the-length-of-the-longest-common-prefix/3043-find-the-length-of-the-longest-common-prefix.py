class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_arr1 = set()
        best = 0
        for a1 in arr1:
            s1 = str(a1)   
            for i in range(len(s1)):
                prefix_arr1.add(s1[:i+1])
        print(prefix_arr1)
        
        for a2 in arr2:
            s2 = str(a2)
            for i in range(len(s2)):
                if s2[:i+1] in prefix_arr1:
                    best = max(best,i+1)
        return best
            