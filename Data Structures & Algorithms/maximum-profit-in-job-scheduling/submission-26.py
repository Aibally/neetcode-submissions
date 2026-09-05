from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        dp=[0]*n # best profit up to i (does not have to include i)
        jobs = [(startTime[i],endTime[i],profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        dp[0] = jobs[0][2]
        endTimes = [jobs[i][1] for i in range(n)]
        # index of the first bigger element than x
        def bisect_right(T,x):
            low = 0
            high = len(T)
            while low<high:
                mid = (low+high) // 2
                if T[mid]<=x:
                    low = mid+1
                else:
                    high = mid
            return low

        for i in range(1,n):
            curr_start, curr_end, curr_profit = jobs[i]
            j = bisect_right(endTimes,curr_start)-1
            include_profit = curr_profit
            if j != -1:
                include_profit += dp[j]
            dp[i] = max(dp[i-1], include_profit)
        return dp[n-1]
            
                