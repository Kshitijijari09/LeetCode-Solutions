class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_A = s1.split()
        words_B = s2.split()

        # Count the occurrences of each word in both sentences
        count_A = Counter(words_A)
        count_B = Counter(words_B)

        # Find uncommon words from sentence A
        uncommon_A = {word for word in count_A if count_A[word] == 1 and word not in count_B}

        # Find uncommon words from sentence B
        uncommon_B = {word for word in count_B if count_B[word] == 1 and word not in count_A}

        # Return the list of uncommon words from both sentences
        return list(uncommon_A.union(uncommon_B))