class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        
        days = 0
        print(jobs,workers)
        for j, w in zip(jobs, workers):
            print(j + w -1, w)
            days = max((j + w - 1) // w, days)
        return days