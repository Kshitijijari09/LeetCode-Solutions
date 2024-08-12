class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastvaluemerged = merged[-1][1]
            if start <= lastvaluemerged:
                print(lastvaluemerged, end)
                merged[-1][1] = max(lastvaluemerged, end)
                print(lastvaluemerged)
            else:
                merged.append([start, end])
        return merged