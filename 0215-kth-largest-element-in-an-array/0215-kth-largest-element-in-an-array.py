class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-1*(n) for n in nums]
        print(maxHeap)
        heapq.heapify(maxHeap)
        print(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        
        return -maxHeap[0]