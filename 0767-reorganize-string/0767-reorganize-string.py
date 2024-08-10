class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        max_count, letter = 0, ''
        
        for char, counts in char_counts.items():
            if counts > max_count:
                max_count = counts
                letter = char
        if max_count > (len(s)+1) // 2:
            return ""
        ans = [""]*len(s)
        index = 0
        
        while char_counts[letter] != 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1
        
        for char, counts in char_counts.items():
            while counts > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                counts -= 1
        print(ans)
        return ''.join(ans)
                

        
        