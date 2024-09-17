class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        print(count)
        for n , c in count.items():
            freq[c].append(n)
        print(freq)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # # from collections import Counter
        # count = Counter(nums)  # Count each number's frequency
        # # Create a list of (frequency, num) tuples and sort it
        # freq_list = sorted(count.items(), key=lambda x: -x[1])
        # print(freq_list)
        # # Extract the top k elements
        # return [num for num, freq in freq_list[:k]]