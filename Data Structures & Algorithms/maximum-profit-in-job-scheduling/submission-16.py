class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        jobs = [(startTime[i],endTime[i],profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        dp = [jobs[i][2] for i in range(n)]

        for i in range(1,n):
            job_curr = jobs[i]
            for j in range(i):
                job_last = jobs[j]
                if job_curr[0] >= job_last[1]:
                    dp[i] = max(dp[i],dp[j]+job_curr[2])

        return max(dp)
                