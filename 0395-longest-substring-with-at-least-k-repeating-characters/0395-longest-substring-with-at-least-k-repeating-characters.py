class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        problematic_letters = []
        valid = True
        counter = Counter(s)
        print(counter)
        for letter in counter:
            if counter[letter] < k:
                problematic_letters.append(letter)
                valid = False
        print(problematic_letters)
        if valid:
            return len(s)

        for letter in problematic_letters:
            s = s.replace(letter, ' ')
            print(s)
        strings_after_divide = s.split()
        print(strings_after_divide)

        ans = 0
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans